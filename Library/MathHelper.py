class MathHelper:

    def __init__(self):
        super().__init__()

    def MeanBetween(array, index0, index1):

        """
        Returns mean between two index values in the array.
        """

        array = array[int(index0) : int(index1)]
        return (min(array) + max(array)) / 2

    def AvgBetween(array, index0, index1):

        """
        Returns average between two index values in the array.
        """

        array = array[int(index0) : int(index1)]
        return sum(array) / len(array)

    def DiffBetween(array, index0, index1):

        """
        Returns differential between two index values in the array.
        """

        array = array[int(index0) : int(index1)]
        return array[int(-1)] - array[int(0)]