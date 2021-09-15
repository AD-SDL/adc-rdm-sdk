class ADCError(Exception):

    def __init__(self, error):
        self.error = error
        super().__init__(self.error)
