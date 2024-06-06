import subprocess
import sys

class BashScriptRunner:
    def __init__(self, script_name):
        self.script_name = script_name

    def run_script(self, input_data):
        try:
            # Define the command to run the Bash script
            bash_command = ['bash', self.script_name]

            # Start the process and connect to its standard input/output/error pipes
            process = subprocess.Popen(bash_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Send input data to the script
            stdout, stderr = process.communicate(input=input_data)

            # Get the return code of the process
            return_code = process.returncode

            return stdout, stderr, return_code
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error while running the script: {e}")
        except FileNotFoundError:
            raise RuntimeError(f"Script '{self.script_name}' not found.")
        except Exception as e:
            raise RuntimeError(f"An error occurred: {e}")

# Example usage
def main():
    try:
        script_runner = BashScriptRunner('your_script.sh')
        input_data = "your_input_here"
        stdout, stderr, return_code = script_runner.run_script(input_data)

        print("Standard output:")
        print(stdout)

        print("Standard error:")
        print(stderr)

        print("Return code:")
        print(return_code)
    except KeyboardInterrupt:
        print("Process interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    sys.exit(0)
