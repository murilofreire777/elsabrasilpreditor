import PySimpleGUI as sg
import numpy as np
import pandas as pd
from Config import Config
from Predictor import Predictor

class PredictorApp:
    def __init__(self):
        self.predictor = Predictor()
        self.config = Config()
        self.window = None
        sg.theme('BlueMono') 
        self.create_main_window()

    def create_main_window(self):
        biosex_options = list(self.config.GetBiologicalSexOpts().keys())
        agegroup_options = list(self.config.GetAgeGroupOpts().keys())
        ethnic_options = list(self.config.GetEthnicOpts().keys())
        marriage_options = list(self.config.GetMarriageStatusOpts().keys())
        schooling_options = list(self.config.GetLevelOfSchoolingOpts().keys())

        smoking_options = list(self.config.GetSmokingOpts().keys())
        drinking_options = list(self.config.GetExcessDrinkingOpts().keys())
        physical_activity_options = list(self.config.GetPhysicalActivityOpts().keys())
        fruits_consume_options = list(self.config.GetFruitsConsumeOpts().keys())
        vegetable_consume_options = list(self.config.GetVegetableConsumeOpts().keys())

        prediction_button = sg.Button("Exibir resultados", font=('Arial', 14), pad=((3, 3), (5, 5)), disabled=True, button_color=('white', 'darkblue'))

        socioeconomic_layout = [
            [sg.Text("Sexo biológico:", font=('Arial', 14), size=(25, 1)), sg.Combo(biosex_options, enable_events=True, size=(20, 1), key="sexo", font=('Arial', 12))],
            [sg.Text("Grupo etário:", font=('Arial', 14), size=(25, 1)), sg.Combo(agegroup_options, enable_events=True, size=(20, 1), key="grupo etário", font=('Arial', 12))],
            [sg.Text("Raça/Cor:", font=('Arial', 14), size=(25, 1)), sg.Combo(ethnic_options, enable_events=True, size=(20, 1), key="raça/cor", font=('Arial', 12))],
            [sg.Text("Estado civil:", font=('Arial', 14), size=(25, 1)), sg.Combo(marriage_options, enable_events=True, size=(20, 1), key="situação conjugal", font=('Arial', 12))],
            [sg.Text("Grau de escolaridade:", font=('Arial', 14), size=(25, 1)), sg.Combo(schooling_options, enable_events=True, size=(20, 1), key="grau de escolaridade", font=('Arial', 12))]
        ]

        lifestyle_layout = [
            [sg.Text("Tabagismo:", font=('Arial', 14), size=(25, 1)), sg.Combo(smoking_options, enable_events=True, size=(20, 1), key="tabagismo", font=('Arial', 12))],
            [sg.Text("Consumo excessivo de álcool:", font=('Arial', 14), size=(25, 1)), sg.Combo(drinking_options, enable_events=True, size=(20, 1), key="bebedor excessivo", font=('Arial', 12))],
            [sg.Text("Prática diária de atividade física:", font=('Arial', 14), size=(25, 1)), sg.Combo(physical_activity_options, enable_events=True, size=(20, 1), key="prát. de ativ. física", font=('Arial', 12))],
            [sg.Text("Consume verduras diariamente:", font=('Arial', 14), size=(25, 1)), sg.Combo(vegetable_consume_options, enable_events=True, size=(20, 1), key="cons. diário verduras", font=('Arial', 12))],
            [sg.Text("Consume frutas diariamente:", font=('Arial', 14), size=(25, 1)), sg.Combo(fruits_consume_options, enable_events=True, size=(20, 1), key="cons. diário frutas", font=('Arial', 12))]
        ]

        title = "\nPreditor para Hipertensão e Diabetes"
        layout = [
             [sg.Image(filename='elsa.png'),
              sg.Multiline(default_text=title, size=(45, 3), font=("Helvetica", 16, "bold"), 
                          disabled=True, border_width=0, background_color=sg.theme_background_color()
                           ,no_scrollbar=True, auto_size_text=True )],
            [sg.Text("", size=(1, 1))],  # Adiciona um espaçamento vertical
            [sg.Frame("Informações socieconômicas", socioeconomic_layout)],
            [sg.Text("", size=(1, 1))],  # Adiciona um espaçamento vertical
            [sg.Frame("Informações do estilo de vida", lifestyle_layout)],
            [sg.Text("", size=(1, 1))],  # Adiciona um espaçamento vertical
            [prediction_button, sg.Button("?", key="-INFO-", font=('Arial', 14), button_color=('white', 'darkgreen'), pad=((3, 3), (5, 5)))],
            [sg.Text("Resultados", size=(24, 1), font=("Helvetica", 16, "bold"))],
            [sg.Text("", size=(35, 1), key="-PREDICTION_HIPERTENSION-", font=("Helvetica", 14, "bold"), relief=sg.RELIEF_RIDGE, background_color='lightblue', text_color='black', pad=(0, 10))],
            [sg.Text("", size=(35, 1), key="-PREDICTION_DIABETES-", font=("Helvetica", 14, "bold"), relief=sg.RELIEF_RIDGE, background_color='lightblue', text_color='black', pad=(0, 10))]
        ]

        self.window = sg.Window("Preditor para Hipertensão Arterial e Diabetes", layout, finalize=True, size=(560,740))

        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Exibir resultados":
                self.do_prediction(values)
            elif event == '-INFO-':
                self.show_info_modal()
            else:
                # Handle other events, such as changes in combo boxes or radio buttons
                self.update_prediction_button(values, prediction_button)

        self.window.close()

    def update_prediction_button(self, values, prediction_button):
        if (
            values["sexo"]
            and values["grupo etário"]
            and values["raça/cor"]
            and values["situação conjugal"]
            and values["grau de escolaridade"]
            and values["tabagismo"]
            and values["bebedor excessivo"]
            and values["prát. de ativ. física"]
            and values["cons. diário verduras"]
            and values["cons. diário frutas"]
        ):
            prediction_button.update(disabled=False)
        else:
            prediction_button.update(disabled=True)

    def do_prediction(self, values):
        for key in values: 
            if key == "sexo": 
               values[key] = self.config.GetBiologicalSexOpts()[values[key]]
            elif key == "grupo etário":
               values[key] = self.config.GetAgeGroupOpts()[values[key]]
            elif key == "raça/cor":
               values[key] = self.config.GetEthnicOpts()[values[key]]
            elif key == "situação conjugal":
               values[key] = self.config.GetMarriageStatusOpts()[values[key]]
            elif key == "grau de escolaridade":
               values[key] = self.config.GetLevelOfSchoolingOpts()[values[key]]
            elif key == "tabagismo":
               values[key] = self.config.GetSmokingOpts()[values[key]]
            elif key == "bebedor excessivo":
               values[key] = self.config.GetExcessDrinkingOpts()[values[key]]
            elif key == "prát. de ativ. física":
               values[key] = self.config.GetPhysicalActivityOpts()[values[key]]
            elif key == "cons. diário verduras":
               values[key] = self.config.GetVegetableConsumeOpts()[values[key]]
            elif key == "cons. diário frutas":
               values[key] = self.config.GetFruitsConsumeOpts()[values[key]]
        #print(pd.DataFrame([values]))
        
        #array_dados = np.array(list(values.values())).reshape(1, -1)
        df = pd.DataFrame([values])
        ordem_colunas = ['sexo', 'grupo etário', 'situação conjugal', 'grau de escolaridade', 'raça/cor', 'prát. de ativ. física', 'cons. diário verduras',   
 'cons. diário frutas', 'tabagismo', 'bebedor excessivo']
        df = df[ordem_colunas]
        prediction_h = self.predictor.PredictHipertension(df)
        if prediction_h[0] == 0:
            result_text_h = "Risco reduzido para Hipertensão Arterial"
        else:
            result_text_h = "Risco aumentado para hipertensão Arterial"

        prediction_d = self.predictor.PredictDiabetes(df)
        if prediction_d[0] == 0:
            result_text_d = "Risco reduzido para Diabetes"
        else:
            result_text_d = "Risco aumentado para Diabetes"

        self.window["-PREDICTION_HIPERTENSION-"].update(result_text_h)
        self.window["-PREDICTION_DIABETES-"].update(result_text_d)
        #print(self.predictor.PredictHipertension(df))
        #print(self.predictor.PredictDiabetes(pd.Series(values)))
        #print(values)

    def show_info_modal(self):
            info_text = (
                "Desenvolvedor: Murilo Freire Oliveira Araújo\n"
                "Descrição: Este aplicativo foi desenvolvido utilizando PySimpleGUI "
                "para prever hipertensão e diabetes baseado em dados do usuário."
            )
            sg.popup('Informações sobre o Aplicativo', info_text)

if __name__ == "__main__":
    app = PredictorApp()
