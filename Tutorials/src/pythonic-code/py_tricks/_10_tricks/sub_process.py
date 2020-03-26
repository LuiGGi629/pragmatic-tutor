import subprocess

# subprocess.run('ls -la', shell=True)
# p1 = subprocess.run(['ls', '-la'])
# p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
# p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)
# print(p1.args)
# print(p1.returncode)
# print(p1.stdout.decode())
# print(p1.stdout)

# with open('test.log', 'w') as file:
#     p1 = subprocess.run(['ls', '-la'], stdout=file, text=True)

# p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)
# p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True, check=True)
# p1 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)
# print(p1.returncode)
# print(p1.stderr)

# p1 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True)
# # print(p1.stdout)
#
# p2 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout)
# print(p2.stdout)

p1 = subprocess.run('cat test.txt | grep -n test', shell=True, capture_output=True, text=True)
print(p1.stdout)
