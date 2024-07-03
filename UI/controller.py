import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        anni = DAO.getAnni()

        self._view.ddyear.options = list(map(lambda x: ft.dropdown.Option(x), anni))

    def handle_graph(self, e):
        if not int(self._view.ddyear.value):
            self._view.create_alert("inserisci anno")
            return
        else:
            anno = int(self._view.ddyear.value)
            giorni = int(self._view.txt_giorni.value)
            print("prila")
            self._model.creaGrafo(anno, giorni)
            self._view.txt_result.controls.append(ft.Text(f"nodi: {self._model.grafoDetails()[0]}, archi: {self._model.grafoDetails()[1]}"))
            pesi = self._model.pesiNodi()
            for peso in pesi:
                self._view.txt_result.controls.append(ft.Text(f"nodo {peso[0]}, peso: {peso[1]}"))
            self._view.update_page()

    def handle_search(self, e):
        pass