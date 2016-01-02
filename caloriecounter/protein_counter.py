# protein_counter

class ProteinCounter:

    def __init__(self, bodyweight=90, units='kg'):
        """Set base attributes."""
        self.bodyweight=bodyweight
        self.units=units

    def protein(self, bodyweight=None):
        """
        Calculate the total grams of protein to consume
        given bodyweight.

        The ratio is 2.2 grammes or protein for every 1 kg of bodyweight.
        """
        if self.units == 'kg' or bodyweight is not None:
            return 2.2 * (bodyweight or self.bodyweight)
        else:
            print('Using default value of bodyweight and \'kg\' as unit')
            return 1 * self.bodyweight
