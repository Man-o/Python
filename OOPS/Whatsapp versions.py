class WhatsAppV1:
    def __init__(self,Name,Dp,Dm):
        self.Name=Name
        self.Dp=Dp
        self.Dm=Dm
    def features(self):
        print(f'Name-{self.Name}')
        print(f'Dp-{self.Dp}')
        print(f'Dm-{self.Dm}')
class WhatsAppV2(WhatsAppV1):
    def __init__(self,Name,Dp,Dm,Vmsg,Status,Acall):
        super().__init__(Name,Dp,Dm)
        self.Vmsg=Vmsg
        self.Status=Status
        self.Acall=Acall
    def features(self):
        super().features()
        print(f'Vmsg-{self.Vmsg}')
        print(f'Status-{self.Status}')
        print(f'Acall-{self.Acall}')
class WhatsAppV3(WhatsAppV2):
    def __init__(self,Name,Dp,Dm,Vmsg,Status,Acall,Vcall,Payments):
        super().__init__(Name,Dp,Dm,Vmsg,Status,Acall)
        self.Vcall=Vcall
        self.Payments=Payments
    def features(self):
        super().features()
        print(f'Vcall-{self.Vcall}')
        print(f'Payments-{self.Payments}')
obj=WhatsAppV3('Mano','Yes','Yes','No','No','No','Yes','No')
obj.features()
    
        
