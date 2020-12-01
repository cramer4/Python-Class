def make_shirt(size='l', message='i love python'):
    print(f"Made shirt that says '{message.title()}' and is size {size.upper()}.")

make_shirt()
make_shirt(size='m')
make_shirt(size='xl', message='python rocks!')