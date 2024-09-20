walker interact {
    can return_message with `root entry {
        report {
            "response": "Hello, world!"
        };
    }
}

walker interact_with_body {
    has name: str;

    can return_message with `root entry {
        report {
            "response": "Hello, " + self.name + "!"
        };
    }
}

walker add_two_numbers {
    has number1: float;
    has number2: float;

    can return_message with `root entry {
        report {
            "response": self.number1 + self.number2
        };
    }
}

walker strings {
    has string: str;
    can is_palindrome with `root entry {
        l = 0;
        r = len(self.string) - 1;

        response = f"'{self.string}' is a palindrome"; 
        while l < r {
            if self.string[l] != self.string[r] {
                response = f"'{self.string}' is not a palindrome";
                break;
            }
            l += 1;
            r -= 1;
        }

        report {
            "response": response
        };
    }
}