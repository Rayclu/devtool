import sys
import commands.new as new, commands.run as run, commands.doctor as doc
def main():
    if len(sys.argv) < 2:
        print("Uso: devtool <command>")
        print("Comandos: new, doctor")
        return

    cmd = sys.argv[1]
    try:
        match cmd:
            case "new":
                new.run(args=sys.argv[2:])
            case "search":
                doc.run()
            case _:
                raise "Invalid option"
                pass
    except "InvalidOption":
        print("Sorry, but, the command typed are invalid. Please select a valid option")
main()