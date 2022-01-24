from numbers import Number, Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + tuple(-i for i in other.coefficients[common:])

            return Polynomial(coefs)

        elif isinstance(other, Number):
            tuple_first = (self.coefficients[0] - other,)
            return Polynomial(tuple_first + self.coefficients[1:])
        
        else:
            return NotImplemented

    def __rsub__(self, other):
        coefs = tuple(-i for i in (self - other).coefficients)
        return Polynomial(coefs)
    
    def __mul__(self, other):
        if isinstance(other, Polynomial):
            new_deg = self.degree() + other.degree() + 1
            coefs = [0] * new_deg
            for i in range(0, self.degree()+1):
                for j in range(0, other.degree()+1):
                    coefs[i+j] += self.coefficients[i] * other.coefficients[j]
            
            return Polynomial(tuple(coefs))

        elif isinstance(other, Number):
            coefs = tuple(other * i for i in self.coefficients)
            return Polynomial(coefs)

        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        if isinstance(other, Integral):
            temp1 = Polynomial(self.coefficients)
            for i in range(1, other):
                 self = temp1*self
            return self
        else:
            return NotImplemented

    def __call__(self, other):
        if isinstance(other, Number):
            total = 0
            for i in range(0, self.degree()+1):
                total += self.coefficients[i]*(other**i)
            return total

        else:
            return NotImplemented