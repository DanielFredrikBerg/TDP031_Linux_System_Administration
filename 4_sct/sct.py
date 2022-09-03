#shebang?
# En shebang börjar med ett hashtecken följt av ett uttropstecken, en absolut filväg till ett körbart program (vanligtvis en interpretator) som kommer exekvera filen. Det går också att lägga till parametrar likt exemplet nedan:
# #!/filväg/till/program param1 param2


# Skriv ett program vilket som första argument får en lista över personers namn, ett per rad, och skapar användarkontot på ert system för var och en av dem.


# Generera ett unikt användarnamn (helst baserat på personens riktiga namn)
import sys
import random
import string
import re
from subprocess import run, Popen, PIPE, check_call

def generate_password(size):
    letters_and_nums = string.ascii_letters + string.digits
    password = [random.choice(letters_and_nums) for i in range(size) ]
    password = ''.join(password)
    return password

    # what about piping?
def generate_username(line):
    if line != '\n':
        line = line.split()
        username = re.sub( '[^a-zA-Z0-9]', '', line[0]+line[-1] )
        username += '#' + str(random.randint(1111,9999))
        return username    

#https://stackoverflow.com/questions/4688441/how-can-i-set-a-users-password-in-linux-from-a-python-script
def user_add(username, password):
    #subprocess.run(['useradd', '-mp', password, username])
    run(['useradd', '-m', username])
    #subprocess.run(['passwd', username, password, password])
    proc = Popen(['passwd', username], stdin=PIPE, stdout=PIPE,stderr=PIPE)
    proc.stdin.write((password + '\n').encode())
    proc.stdin.write(password.encode())
    proc.stdin.flush()
    stdout, stderr = proc.communicate()
    #print(stdout)
    #print(stderr)

def create_user(line):
    username = generate_username(line)
    password = generate_password(8)
    new_user = user_add( username, password )
    print(f"Username: {username}, Password: {password}")

def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        for line in lines:
            create_user(line)

main()

# Lägg till användaren på systemet

# Se till att användaren har en hemkatalog, med eventuella standardfiler i

# Slumpa fram och sätt ett lösenord

# (Sätt upp andra eventuella tjänster)

# Skriv ut användarnamn och lösenord
