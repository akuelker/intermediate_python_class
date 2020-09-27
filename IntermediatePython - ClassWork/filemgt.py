import os #op sys library
if os.path.isfile('test.txt'):
    os.rename('test.txt', 'Jurassic.txt')
else: print("Nope")
