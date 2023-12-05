def parse_arg2(arg):
    args = []

    index = -1
    adding = False
    terminator = " "
    for i in range(len(arg)):
        if arg[i] == terminator and adding:
            terminator = " "
            adding = False
            continue

        if arg[i] == '"' and arg[i - 1] == "\\":
            if adding:
                args[index] += arg[i:]
            else:
                args.append(arg[i:])
                index += 1
                adding = True
        elif arg[i] == '"' and not adding and arg[i - 1] != "\\":
            terminator = '"'
            continue
        elif arg[i] == "\\":
            continue
        else:
            if not adding:
                args.append("")
                index += 1
                adding = True
            args[index] += arg[i]

    return args


# Basic case with double quotes
arg1 = 'command "arg with spaces" value'
print(parse_arg2(arg1))
# Double quotes with an escaped quote inside
arg2 = 'command "arg with escaped \\"quote\\" inside" value'
print(parse_arg2(arg2))

# No quotes, just words
arg3 = "command arg1 arg2 arg3"
print(parse_arg2(arg3))

# Double quotes with an escaped backslash inside
arg4 = 'command "arg with escaped \\\\backslash\\" inside" value'
print(parse_arg2(arg4))

# Single quotes
arg5 = "command 'arg with spaces' value"
print(parse_arg2(arg5))

# Mixed quotes
arg6 = "command \"arg with spaces' value"
print(parse_arg2(arg6))

# Quotes within quotes with escaped quotes
arg7 = 'command "arg with \\"nested\\" quotes" value'
print(parse_arg2(arg7))

# Single quotes within double quotes
arg8 = "command \"arg with 'nested' quotes\" value"
print(parse_arg2(arg8))

# Quotes within quotes with escaped backslashes
arg9 = 'command "arg with \\\\escaped backslashes" value'
print(parse_arg2(arg9))

# Empty string
arg10 = ""
print(parse_arg2(arg10))

# Single word with trailing spaces
arg11 = "command   "
print(parse_arg2(arg11))

# Multiple spaces between words
arg12 = "command  word1   word2     word3"
print(parse_arg2(arg12))
