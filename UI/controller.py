import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        anni = self._model.year
        for a in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(data=a,
                                                               text = a,
                                                               on_click=self.choiceYear))
        self._view.update_page()





    def choiceYear(self,e ):
        if e.control.data is None:
            self.Year = None
        else:
            self.Year = e.control.data

    def handle_graph(self, e):
        giorni = self._view.txt_giorni.value

        try:
            intGiorni = int(giorni)
        except ValueError:
            self._view.create_alert("Inserire un valore numerico")
        if intGiorni < 1 or intGiorni > 180:
            self._view.create_alert("inserire un valore nell'intervallo considerato")
            return
        self._model.buildGraph(self.Year, intGiorni)

        self._view.txt_result.controls.clear()
        nodi, archi = self._model.graph_details()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato!"
                                                     f"#Vertici: {nodi}"
                                                     f"#Archi: {archi}"))

        risultato = self._model.getPesi()
        for r in risultato:
            self._view.txt_result.controls.append(ft.Text(f"{r[0]} --> {r[1]}"))
        self._view.update_page()


    def handle_search(self, e):
        pass