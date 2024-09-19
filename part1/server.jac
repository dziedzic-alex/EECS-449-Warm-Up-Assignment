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

walker is_palindrome {
    has string: str;

    l = 0
    r = len(self.string) - 1

    palindrome = True
    while l < r:
        if self.string[l] != self.string[r]:
            palindrome = False
            break
        l += 1
        r -= 1
    
    can return_message with `root entry {
        report {
            "response": palindrome
        };
    }
}