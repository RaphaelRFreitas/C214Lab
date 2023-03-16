class Veiculo:
    def __init__(self, placa, ano):
        self._placa = placa
        self._ano = ano

    def __init__(self):
        pass

    def getPlaca(self):
        return self._placa

    def getAno(self):
        return self._ano

    def setPlaca(self, placa):
        self._placa = placa

    def setAno(self, ano):
        self._ano = ano

    def exibirDados(self):
        print("Placa: ", self._placa)
        print("Ano: ", self._ano)


class Caminhao(Veiculo):
    def __init__(self, placa, ano, eixos):
        super().__init__(placa, ano)
        self._eixos = eixos

    def getEixos(self):
        return self._eixos

    def setEixos(self, eixos):
        self._eixos = eixos

    def exibirDados(self):
        super().exibirDados()
        print("Eixos: ", self._eixos)


class Onibus(Veiculo):
    def __init__(self, placa, ano, assentos):
        super().__init__(placa, ano)
        self._assentos = assentos

    def getAssentos(self):
        return self._poltronas

    def setAssentos(self, assentos):
        self._poltronas = assentos

    def exibirDados(self):
        super().exibirDados()
        print("Poltronas: ", self._assentos)
