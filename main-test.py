# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 5
        assert Add(5,5) == 11

        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()


# git checkout -b add-test
# git add .
# git commit -m "Adds test  5 + 5 "
# git push --set-upstream origin add-test        