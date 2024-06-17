#!/bin/bash

# Function to encrypt the key
key_encryption() {
    # Generate a random encryption key
    key=$(openssl rand -base64 32)

    # Save the encryption key to a file
    echo "$key" > encryption_key.key

    # Encrypt the key file using a passphrase
    passphrase="MySuperSecurePassphrase"  # Replace with your passphrase
    encrypted_key=$(echo "$key" | openssl enc -aes-256-cbc -pbkdf2 -pass "pass:$passphrase" -base64)

    # Save the encrypted data to a new file
    echo "$encrypted_key" > encrypted_encryption_key.key
}

# Function to send email
send_email() {
    # Get user input for email details
    read -p "Enter sender email address: " sender_email
    read -p "Enter receiver email address: " receiver_email
    read -p "Enter email subject: " subject
    read -p "Enter email message: " message
    attachments=("attachment_1.pdf" "attachment_2.pdf")

    # Load configuration
    config=$(load_config)
    smtp_server=$(echo "$config" | jq -r '.smtp_server')
    smtp_port=$(echo "$config" | jq -r '.smtp_port')
    smtp_username=$(echo "$config" | jq -r '.smtp_username')
    smtp_password=$(echo "$config" | jq -r '.smtp_password')

    # Basic send email
    basic_send_email "$sender_email" "$receiver_email" "$subject" "$message"

    # Send email with attachments
    send_email_with_attachments "$sender_email" "$receiver_email" "$subject" "$message" "${attachments[@]}"
}

# Function to send a basic email
basic_send_email() {
    local sender_email=$1
    local receiver_email=$2
    local subject=$3
    local message=$4

    # Validate email addresses
    if ! [[ $sender_email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        echo "Invalid sender email address."
        exit 1
    fi

    if ! [[ $receiver_email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        echo "Invalid receiver email address."
        exit 1
    fi

    # Create message
    {
        echo "From: $sender_email"
        echo "To: $receiver_email"
        echo "Subject: $subject"
        echo "Content-Type: text/plain; charset=UTF-8"
        echo ""
        echo "$message"
    } > email.txt

    # Connect to SMTP server and send email
    (
        echo "EHLO $smtp_server"
        sleep 1
        echo "AUTH LOGIN"
        sleep 1
        echo "$smtp_username"
        sleep 1
        echo "$smtp_password"
        sleep 1
        echo "MAIL FROM:$sender_email"
        sleep 1
        echo "RCPT TO:$receiver_email"
        sleep 1
        echo "DATA"
        sleep 1
        cat email.txt
        echo ""
        echo "."
        echo "QUIT"
    ) | openssl s_client -quiet -connect "$smtp_server:$smtp_port" -starttls smtp -crlf -ign_eof -CApath /etc/ssl/certs -CAfile /etc/ssl/certs/ca-certificates.crt
}

# Function to send email with attachments
send_email_with_attachments() {
    local sender_email=$1
    local receiver_email=$2
    local subject=$3
    local message=$4
    shift 4
    local attachments=("$@")

    # Validate email addresses
    if ! [[ $sender_email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        echo "Invalid sender email address."
        exit 1
    fi

    if ! [[ $receiver_email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        echo "Invalid receiver email address."
        exit 1
    fi

    # Create message
    {
        echo "From: $sender_email"
        echo "To: $receiver_email"
        echo "Subject: $subject"
        echo "Content-Type: multipart/mixed; boundary=\"boundary\""
        echo ""
        echo "--boundary"
        echo "Content-Type: text/plain; charset=UTF-8"
        echo ""
        echo "$message"
        echo ""
    } > email.txt

    # Attach files
    for attachment in "${attachments[@]}"; do
        echo "--boundary"
        echo "Content-Type: application/octet-stream"
        echo "Content-Disposition: attachment; filename=\"$attachment\""
        echo ""
        cat "$attachment"
        echo ""
    done >> email.txt
    echo "--boundary--" >> email.txt

    # Connect to SMTP server and send email
    (
        echo "EHLO $smtp_server"
        sleep 1
        echo "AUTH LOGIN"
        sleep 1
        echo "$smtp_username"
        sleep 1
        echo "$smtp_password"
        sleep 1
        echo "MAIL FROM:$sender_email"
        sleep 1
        echo "RCPT TO:$receiver_email"
        sleep 1
        echo "DATA"
        sleep 1
        cat email.txt
        echo ""
        echo "."
        echo "QUIT"
    ) | openssl s_client -quiet -connect "$smtp_server:$smtp_port" -starttls smtp -crlf -ign_eof -CApath /etc/ssl/certs -CAfile /etc/ssl/certs/ca-certificates.crt
}

# Function to load config
load_config() {
    config_file_path="config.json" # configuration file
    key_file_path="encrypted_encryption_key.key" # encryption key file
    passphrase=${SMTP_PASSPHRASE:-"MySuperSecurePassphrase"} # passphrase for encryption

    # Decrypt the encryption key using the passphrase
    encrypted_key=$(cat "$key_file_path")
    key=$(echo "$encrypted_key" | openssl enc -d -aes-256-cbc -pbkdf2 -pass "pass:$passphrase" -base64)

    # Load the encrypted configuration file using the decrypted key
    encrypted_data=$(cat "$config_file_path")
    decrypted_data=$(echo "$encrypted_data" | openssl enc -d -aes-256-cbc -pbkdf2 -pass "pass:$key" -base64)
    echo "$decrypted_data"
}

# Main function
main() {
    send_email
}

main
