class Config():
    def __init__(self) -> None:
        self.__biological_sex_opts = { "Masculino" : 1, "Feminino" : 0}
        self.__age_group_opts = {
                                "35-40 anos" : 0,
                                "41-50 anos" : 1,
                                "51-60 anos" : 2,
                                "61-70 anos" : 3,
                                "71-80 anos" : 4,
                                "Mais de 80 anos" : 5}
        self.__ethnic_opts = {
                                "Preta" : 4,
                                "Parda" : 3,
                                "Branca" : 0,
                                "Amarela" : 1,
                                "Indígena" : 2}
        
        self.__marriage_status_opts = {
                                "Casado/Unido" : 0,
                                "Separado/Divorciado" : 1,
                                "Solteiro" : 2,
                                "Viúvo" : 3,
                                "Outro (com união Prévia)" : 4}

        self.__level_of_schooling_opts = {
                                "Até fundamental incompleto" : 3,
                                "Fundamental completo" : 2,
                                "Médio completo" : 1,
                                "Superior completo" : 0}
        self.__smoking_opts = {
            "Não fumante" : 0,
            "Fumante" : 1
        }

        self.__excess_drinking_opts = {
            "Não" : 0,
            "Sim" : 1
        }

        self.__physical_activity_opts = {
            "Não" : 1,
            "Sim" : 0
        }

        self.__fruits_consume_opts = {
            "Não" : 1,
            "Sim" : 0
        }

        self.__vegetables_consume_opts = {
            "Não" : 1,
            "Sim" : 0
        }

    def GetBiologicalSexOpts(self):
        return self.__biological_sex_opts
    
    def GetAgeGroupOpts(self):
        return self.__age_group_opts
    
    def GetEthnicOpts(self):
        return self.__ethnic_opts
    
    def GetMarriageStatusOpts(self):
        return self.__marriage_status_opts
    
    def GetLevelOfSchoolingOpts(self):
        return self.__level_of_schooling_opts
    
    def GetSmokingOpts(self):
        return self.__smoking_opts
    
    def GetExcessDrinkingOpts(self):
        return self.__excess_drinking_opts
    
    def GetPhysicalActivityOpts(self):
        return self.__physical_activity_opts
    
    def GetFruitsConsumeOpts(self):
        return self.__fruits_consume_opts
    
    def GetVegetableConsumeOpts(self):
       return self.__vegetables_consume_opts