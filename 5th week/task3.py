import sys
args = sys.argv[1:]
if args:
    args.sort(key=len)
    print(args[0])
else:
    print("No arguments provided.")
