class Perforator:
    def __init__(self, number_of_revolutions, frequency_of_strokes, color="",
                 producer="", weight=0, length_of_cabel=0, size=""):
        self.number_of_revolutions = number_of_revolutions
        self.frequency_of_strokes = frequency_of_strokes
        self.color = color
        self.producer = producer
        self.weight = weight
        self.length_of_cabel = length_of_cabel
        self.size = size

    def __str__(self):
        return "number_of_revolutions :{},frequency_of_strokes:{},color:{},producer:{}," \
               "length_of_cabel:{}, size:{} ".format(
                self.number_of_revolutions, self.frequency_of_strokes,
                self.color, self.producer, self.weight,
                self.length_of_cabel, self.size
                                                    )

    price = 1000

    @staticmethod
    def price():
        return Perforator.price

    def __del__(self):
        print(0)


o = Perforator(300, 200, 'black')
print(o)
u = Perforator(400, 300, 'green', 'ukr', 5, 0)
print(u)
w = Perforator(450, 250, 'grey', 'pln', 4)
print(w)
print(Perforator.price())
