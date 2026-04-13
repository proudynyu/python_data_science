class Exercices:
    def palindromo(str) -> bool:
        reversed = "".join([str[i] for i in range(len(str)-1, -1, -1)])
        return str.lower() == reversed.lower()

    def convert_to_text(arr_num):
        return "".join(chr(i) for i in arr_num)

    def convert_to_number(str):
        return [ord(i) for i in str]

    def get_intersection(arr_1, arr_2):
        new = []
        for i in arr_1:
            if i in arr_2:
                new.append(i)
        new.sort()
        return new

    def get_union(arr_1, arr_2):
        new = []
        for i in arr_1:
            if i not in arr_2:
                new.append(i)
        for i in arr_2:
            if (i not in arr_1) and (i not in new):
                new.append(i)

        new.sort()
        return new

    def count_character(str):
        m = dict()
        for i in str:
            if m.get(i):
                m[i] += 1
            else:
                m[i] = 1
        return m

class Testing(Exercices):
    def test_convert_to_number():
        text = 'a cat'
        expect = [97, 32, 99, 97, 116]
        assert(Exercices.convert_to_number(text) == expect)

    def test_convert_to_text():
        arr = [97, 32, 99, 97, 116]
        expect = 'a cat'
        assert(Exercices.convert_to_text(arr) == expect)

    def test_palindromo():
        iseq =  Exercices.palindromo("ana")
        noteq = Exercices.palindromo("igor")
        eq = Exercices.palindromo("!ab123 4 321ba!")

        assert(iseq == True)
        assert(eq == True)
        assert(noteq == False)

    def test_get_intersection():
        arr_1 = [1,2,3,4]
        arr_2 = [4,5,6,1]
        expect = [1, 4]
        t = Exercices.get_intersection(arr_1, arr_2)
        assert(t ==  expect)

    def test_get_union():
        arr_1 = [1,2,3,4]
        arr_2 = [4,5,6,1]
        expect = [2, 3, 5, 6]
        t = Exercices.get_union(arr_1, arr_2)
        assert(t == expect)

    def test_count_characters():
        text = "asdasdasd"
        expect = dict(a= 3, s= 3, d = 3)
        t = Exercices.count_character(text)
        assert(t == expect)

if __name__ == '__main__':
    Testing.test_palindromo()
    Testing.test_convert_to_number()
    Testing.test_convert_to_text()
    Testing.test_get_intersection()
    Testing.test_get_union()
    Testing.test_count_characters()