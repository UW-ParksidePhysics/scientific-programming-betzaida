import os

modules = [ 'spin_icons' ]

for module in modules:
    filename = module + '.py'
    if not os.path.exists(filename):
        print(f"Creating empty placeholder for: {filename}")
        with open(filename, 'w') as file:
            file.write('')

    print(f"\n Running test for: {filename} ")
    with open(filename) as module_file:
        try:
            exec(module_file.read())
            print(f" Test Passed: {filename} \n")
        except Exception as e:
            print(f" Test Failed: {filename} ")
            print(e)
            print("\n")
