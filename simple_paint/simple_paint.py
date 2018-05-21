#-*- coding:utf-8 -*-
from kivy.app import App # gerekli olna modülleri içe aktardık
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line,Color,Rectangle,Ellipse
from kivy.uix.button import Button
from kivy.lang import Builder
Builder.load_file("simple_app.kv")

class main(FloatLayout):
    pass

class select(BoxLayout):
    def renk_red(self):
        global renk
        renk = "red"

    def renk_green(self):
        global renk
        renk = "yesil"

    def renk_blue(self):
        global renk
        renk = "mavi"
    def sekil_core(self):
        global sekil
        sekil = "kare"
    def sekil_elips(self):
        global sekil
        sekil = "elips"
    def sekil_line(self):
        global sekil
        sekil = "cizgi"
        

class drawing(BoxLayout):
    global renk
    global sekil

    renk = "beyaz"
    sekil = "cizgi"
    def on_touch_down(self,touch): #down ile basıldığına işle mdevreye girecektir
        
        with self.canvas: # ardından canvas ile yap dedik
            if renk == "red":
                Color(1,0,0)
            elif renk == "yesil":
                Color(0,1,0)
            elif renk == "mavi":
                Color(0,0,1)
            else:
                Color(1,1,2)

            #Color(1,1,1) # canvasın içinden renk seçimini yaptık

            
            if sekil == "cizgi":
                touch.ud["Line"] = Line(points = (touch.x, touch.y)) #daha sonra ise line x ve y koordinatlari ile aldık yani bastığımız yerden itibaren çizmeye başlayacaktır
            elif sekil == "kare":
                touch.ud["kare"] = Rectangle(pos = (touch.x,touch.y),size=(10,10))
            elif sekil == "elips":
                touch.ud["elips"] = Ellipse(pos = (touch.x,touch.y), size=(10,10))
                
    def on_touch_move(self,move):# daha sonra move ile taşıma yani sürükleme işlemi yaptık 
        if sekil == "cizgi":
            move.ud["Line"].points += (move.x,move.y) # bu da diğerine benzer  bir şekilde sürükleme için koordinatları aldık
        elif sekil == "kare":
            move.ud["kare"].pos = (move.x,move.y)
        elif sekil == "elips":
            move.ud["elips"].pos = (move.x,move.y)
            

class paint(App): # ardından ana sınıfızı tanımladık
    
    def build(self): # asıl işlerin yürüdüğü fonksiyın burası
        self.buton = Button(text = ("Temizle"))
        self.buton.bind(on_press = self.temizle)
        self.main = main() #ilk önce maini faklı bir değişkene atadık
        self.select = select() # aynı
        self.draw = drawing()# aynı
        self.select.add_widget(self.buton)
        self.main.add_widget(self.draw) # burda önemli bir nokta var ki o da hangisini önce tanımlarsaınız ilk önde o olur 
        self.main.add_widget(self.select) # bu ise arkada kalır. böylelikle tuş takımını üstünü çizemiyoruz

        return self.main # daha sonra kv dosyamızın içe aktarıldığı main adındaki sınıfmız döndürdğük

    def temizle(self,obj):
        self.draw.canvas.clear()                            
if __name__ == '__main__':
    paint().run()
