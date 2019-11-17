# Class to read 
class Mesh:
    def __init__(self, filename, color=[0., 0., 0.]):

        f = open(filename, 'r')
        self.vertices = []
        self.indices = []
        self.model = ""
        nb_vertices = 0
        nb_faces = 0

        idx = 0

        with f as src:
            data = json.load(src)
            self.vertices = data['vertices']
            self.indices = data['faces']
            self.model = data['car_type']



if __name__ == '__main__':
    path_model = ''
    mesh = Mesh(path_model)