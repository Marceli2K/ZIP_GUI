#!/usr/bin/env python3
"""
TODO list

"""

import os
import sys
import subprocess
from subprocess import Popen, PIPE, STDOUT
from time import sleep

# from gi import require_version as gi_require_version

# gi_require_version('Gtk', '3.0')

from gi.repository import Gtk
import ntpath

NAME = 'GtkApp'
__version__ = '0.0.1'
VERSIONSTR = '{} v. {}'.format(NAME, __version__)


class App(Gtk.Window):
    """ Main window with all components. """

    def __init__(self):
        self.inputFromDialog = ""
        self.polecenie = ""
        self.polecenieTarget = ""
        self.poleceniePATH = ""
        self.polecenieNameAfterZip = ""
        self.PATH = ""
        self.polecenieNazwaPliku = ""
        self.czyNazwaTaSamCOPlik = 1
        self.polecenieCompression = ""
        self.polecenieIntegralTest = ""
        self.polecenieDeleteInZip = ""
        self.labelOutput = ""
        self.polecenieNazwaKATALOGU = ""
        self.polecenieNazwaPlikuZIP = ""
        self.fileToDelete = ""
        self.commentToAdd = ""

        self.TMPon_toggleButton2_toggled = 0
        self.TMPon_toggleButton1_toggled = 0
        Gtk.Window.__init__(self)

        self.builder = Gtk.Builder()
        gladefile = '/home/kali/Desktop/ZIPgu_pythron/KOWALCZYK_ZIPgui.ui'
        if not os.path.exists(gladefile):
            # Look for glade file in this project's directory.
            gladefile = os.path.join(sys.path[0], gladefile)

        try:
            self.builder.add_from_file(gladefile)
        except Exception as ex:
            print('\\nError building main window!\\n{}'.format(ex))
            sys.exit(1)
        # Get gui objects

        # Get gui objects
        self.AboutImagemenuitem = self.builder.get_object('AboutImagemenuitem')
        self.helpMenuitem1 = self.builder.get_object('helpMenuitem1')
        self.ExitImagemenuitem = self.builder.get_object('ExitImagemenuitem')
        self.SaveImagemenuitem = self.builder.get_object('SaveImagemenuitem')
        self.TargetComboboxtext = self.builder.get_object('TargetComboboxtext')
        self.alignment1 = self.builder.get_object('alignment1')
        self.alignment10 = self.builder.get_object('alignment10')
        self.alignment11 = self.builder.get_object('alignment11')
        self.alignment13 = self.builder.get_object('alignment13')
        self.alignment14 = self.builder.get_object('alignment14')
        self.alignment15 = self.builder.get_object('alignment15')
        self.alignment16 = self.builder.get_object('alignment16')
        self.alignment17 = self.builder.get_object('alignment17')
        self.alignment18 = self.builder.get_object('alignment18')
        self.alignment19 = self.builder.get_object('alignment19')
        self.alignment2 = self.builder.get_object('alignment2')
        self.alignment20 = self.builder.get_object('alignment20')
        self.alignment21 = self.builder.get_object('alignment21')
        self.alignment22 = self.builder.get_object('alignment22')
        self.alignment3 = self.builder.get_object('alignment3')
        self.alignment4 = self.builder.get_object('alignment4')
        self.alignment5 = self.builder.get_object('alignment5')
        self.alignment6 = self.builder.get_object('alignment6')
        self.alignment7 = self.builder.get_object('alignment7')
        self.alignment8 = self.builder.get_object('alignment8')
        self.alignment9 = self.builder.get_object('alignment9')
        self.compressionLevel = self.builder.get_object('compressionLevel')
        self.dDeleteInZIPCheckbutton = self.builder.get_object('dDeleteInZIPCheckbutton')
        self.hbox1 = self.builder.get_object('hbox1')
        self.hbox2 = self.builder.get_object('hbox2')
        self.hbox3 = self.builder.get_object('hbox3')
        self.hpaned1 = self.builder.get_object('hpaned1')
        self.hpaned2 = self.builder.get_object('hpaned2')
        self.hpaned3 = self.builder.get_object('hpaned3')
        self.hpaned4 = self.builder.get_object('hpaned4')
        self.hpaned5 = self.builder.get_object('hpaned5')
        self.hpaned6 = self.builder.get_object('hpaned6')
        self.hpaned7 = self.builder.get_object('hpaned7')
        self.hpaned8 = self.builder.get_object('hpaned8')
        self.label1 = self.builder.get_object('label1')
        self.label2 = self.builder.get_object('label2')
        self.label3 = self.builder.get_object('label3')
        self.label4 = self.builder.get_object('label4')
        self.label5 = self.builder.get_object('label5')
        self.label6 = self.builder.get_object('label6')
        self.menu1 = self.builder.get_object('menu1')
        self.menu2 = self.builder.get_object('menu2')
        self.menu3 = self.builder.get_object('menu3')
        self.menubar1 = self.builder.get_object('menubar1')
        self.menuitem1 = self.builder.get_object('menuitem1')
        self.menuitem2 = self.builder.get_object('menuitem2')
        self.menuitem4 = self.builder.get_object('menuitem4')
        self.nameOptionRadiobutton1 = self.builder.get_object('nameOptionRadiobutton1')
        self.nameOptionRadiobutton2 = self.builder.get_object('nameOptionRadiobutton2')
        self.plikLubKatalog = self.builder.get_object('plikLubKatalog')
        self.plikLubKatalog1 = self.builder.get_object('plikLubKatalog1')
        self.plikLubKatalog2 = self.builder.get_object('plikLubKatalog2')
        self.resultLabel = self.builder.get_object('resultLabel')
        self.runButton = self.builder.get_object('runButton')
        self.scrolledwindow1 = self.builder.get_object('scrolledwindow1')
        self.tIntegralTestCheckbutton = self.builder.get_object('tIntegralTestCheckbutton')
        self.toggleButton2 = self.builder.get_object('toggleButton2')
        self.trybToggleButton1 = self.builder.get_object('trybToggleButton1')
        self.viewport1 = self.builder.get_object('viewport1')
        self.viewport2 = self.builder.get_object('viewport2')
        self.vpaned1 = self.builder.get_object('vpaned1')
        self.vpaned2 = self.builder.get_object('vpaned2')
        self.vpaned3 = self.builder.get_object('vpaned3')
        self.vpaned4 = self.builder.get_object('vpaned4')
        self.vpaned5 = self.builder.get_object('vpaned5')
        self.window1 = self.builder.get_object('window1')

        self.textInput = self.builder.get_object('textInput')
        self.OK = self.builder.get_object('OK')
        self.Anuluj = self.builder.get_object('Anuluj')
        self.textbuffer1 = self.builder.get_object('textbuffer1')

        self.dialogInput = self.builder.get_object('dialogInput')

        self.builder.connect_signals(self)
        self.window1.show_all()

        self.plikLubKatalog.SELECT_FOLDER = False
        Gtk.FileChooserAction.OPEN = True

        # stan przyciskow
        self.trybToggleButton1Stan = self.builder.get_object("trybToggleButton1")
        self.toggleButton2Stan = self.builder.get_object("toggleButton2")
        self.guiFunctionaVisible()

    def setPolecenie(self, x):
        self.polecenie = x

    def setPolecenieTarget(x):
        polecenieTarget = x

    def setPoleceniePATH(self, x):
        self.poleceniePATH = x

    def setPolecenieNameAfterZip(self, x):
        self.polecenieNameAfterZip = x

    def setPATH(self, x):
        self.PATH = x

    def setSensitivePlikLubKatalog(self, y):

        self.plikLubKatalog.set_sensitive(y)

    def on_AboutImagemenuitem_activate(self, widget, user_data=None):
        """ Handler for AboutImagemenuitem.activate. """
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Tworca : Marceli Kowalczyk",
        )
        dialog.format_secondary_text(
            "Jest to graficzny interfejs programu zip"
        )
        dialog.run()
        print("INFO dialog closed")
        dialog.destroy()
        pass

    def on_helpMenuitem1_activate(self, widget, user_data=None):
        """ Handler for AboutImagemenuitem.activate. """
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Aby zaczc uzytkowanie programu nalezy : ",
        )
        dialog.format_secondary_text(
            "1) Wybrac opcje czy chcesz pracowac z istniejacym plikiem zip\n"
            "2) Wybrac plik oraz interesujace nas opcje!\n"
            "Spojrz jakie to proste"
        )
        dialog.run()
        print("INFO dialog closed")
        dialog.destroy()
        pass

    def on_ExitImagemenuitem_activate(self, widget, user_data=None):
        """ Handler for ExitImagemenuitem.activate. """
        # WYLACZ OPROGRAMOWANIE
        self.window1.destroy()
        sys.exit()
        pass

    def on_CompressionComboboxtext_changed(self, widget, user_data=None):
        model = widget.get_model()
        active = widget.get_active()
        if active >= 0:
            self.polecenieCompression = ""
            code = model[active][1]
            print('The code of the selected color is {}'.format(code))
            if format(code) == '11':
                pass
            elif format(code) == '0':
                self.polecenieCompression = self.polecenieCompression.join(" -0")
            elif format(code) == '1':
                self.polecenieCompression = self.polecenieCompression.join(" -1")
            elif format(code) == '2':
                self.polecenieCompression = self.polecenieCompression.join(" -2")
            elif format(code) == '3':
                self.polecenieCompression = self.polecenieCompression.join(" -3")
            elif format(code) == '4':
                self.polecenieCompression = self.polecenieCompression.join(" -4")
            elif format(code) == '5':
                self.polecenieCompression = self.polecenieCompression.join(" -5")
            elif format(code) == '6':
                self.polecenieCompression = self.polecenieCompression.join(" -6")
            elif format(code) == '7':
                self.polecenieCompression = self.polecenieCompression.join(" -7")
            elif format(code) == '8':
                self.polecenieCompression = self.polecenieCompression.join(" -8")
            elif format(code) == '9':
                self.polecenieCompression = self.polecenieCompression.join(" -9")
        else:
            print('No color selected')

        pass

    def on_SaveImagemenuitem_activate(self, widget, user_data=None):
        """ Handler for SaveImagemenuitem.activate. """
        pass

    def on_Anuluj_clicked(self, widget, user_data=None):
        """ Handler for SaveImagemenuitem.activate. """
        self.dialogInput.hide()
        self.textbuffer1.set_text("")
        # self.dialogInput.destroy()
        pass

    def on_OK_clicked(self, widget, user_data=None):
        """ Handler for SaveImagemenuitem.activate. """
        self.inputFromDialog = self.textbuffer1.get_text(self.textbuffer1.get_start_iter(),
                                                         self.textbuffer1.get_end_iter(), True)
        print(self.inputFromDialog)
        self.dialogInput.hide()
        self.textbuffer1.set_text("")
        # self.dialogInput.destroy()
        pass

    def on_textInput_add(self, widget, user_data=None):
        """ Handler for SaveImagemenuitem.activate. """
        print()
        pass

    def on_textbuffer1_changed(self, widget, user_data=None):
        """ Handler for SaveImagemenuitem.activate. """

        pass

    def on_TargetComboboxtext_changed(self, widget, user_data=None):
        model = widget.get_model()
        active = widget.get_active()
        self.plikLubKatalog.set_sensitive(False)
        if active >= 0:
            self.polecenieTarget = ""
            code = model[active][1]
            print('The code of the selected color is {}'.format(code))
            if format(code) == '11':
                pass
            elif format(code) == '2':
                self.polecenieTarget = self.polecenieTarget.join(" -sf")
            elif format(code) == '3':
                self.polecenieTarget = self.polecenieTarget.join(" -z")
                self.dialogInput.run()
                self.commentToAdd = self.inputFromDialog
        else:
            self.polecenieTarget = ""
            print('No color selected')

        """ Handler for TargetComboboxtext.changed. """
        pass

    def on_dDeleteInZIPCheckbutton_toggled(self, widget, user_data=None):
        """ Handler for dDeleteInZIPCheckbutton.toggled. """
        active = self.ifActiveDeleteInZip()
        if (active):
            self.dialogInput.run()
            self.fileToDelete = self.inputFromDialog
            self.polecenieDeleteInZip = " -d"
        else:
            self.polecenieDeleteInZip = ""
        pass

    def on_iOptionJPGRadiobutton_toggled(self, widget, user_data=None):
        """ Handler for iOptionJPGRadiobutton.toggled. """
        pass

    def on_plikLubKatalog1_choosen(self, widget, user_data=None):
        """ Handler for plikLubKatalog.file-set. """
        self.PATH = " " + widget.get_file().get_path()
        print("self.PATH", self.PATH)
        self.poleceniePATH = ""
        self.poleceniePATH = self.polecenieNameAfterZip
        print("self.poleceniePATH ", self.poleceniePATH)
        self.polecenieNazwaPliku = ntpath.basename(self.PATH)
        print("self.polecenieNazwaPliku ", self.polecenieNazwaPliku)

        pass

    def on_plikLubKatalog2_choosen(self, widget, user_data=None):
        """ Handler for plikLubKatalog.file-set. """
        self.PATH = " " + widget.get_file().get_path()
        print("self.PATH", self.PATH)
        self.poleceniePATH = ""
        self.poleceniePATH = self.polecenieNameAfterZip
        print("self.poleceniePATH ", self.poleceniePATH)
        self.polecenieNazwaKATALOGU = ntpath.basename(self.PATH)
        print("self.polecenieNazwapolecenieNazwaKATALOGU ", self.polecenieNazwaKATALOGU)

        pass

    def on_plikZip_choosen(self, widget, user_data=None):
        """ Handler for plikLubKatalog.file-set. """
        self.PATH = " " + widget.get_file().get_path()
        print("self.PATH", self.PATH)
        self.poleceniePATH = ""
        self.poleceniePATH = self.polecenieNameAfterZip
        print("self.poleceniePATH ", self.poleceniePATH)
        self.polecenieNazwaPlikuZIP = ntpath.basename(self.PATH)
        if (not self.PATH.lower().endswith(".zip")):
            self.showCummnikate("W tej opcji naley wybraplik o rozszerzeniu zip!!",
                                "Bez tego nie da sie uruchomic danej opcji")
            print("self.polecenieNazwaPlikuZIP ", self.polecenieNazwaPlikuZIP)
            self.polecenieNazwaPlikuZIP = ""
        else:
            self.setSensitivePlikLubKatalog(False)

        pass

    def on_rOptionRadiobutton_toggled(self, widget, user_data=None):
        """ Handler for rOptionRadiobutton.toggled. """
        pass

    def on_runButton_clicked(self, widget, user_data=None):
        czyWybranoPlik = 1
        czyPlikToZIP = 0
        zip = "zip "
        tmpfileToDelete = 0
        self.polecenie = ""
        """ Handler for runButton.clicked. """
        ### Obsuga nazwy pliku
        if (self.czyNazwaTaSamCOPlik == 1):
            if (self.polecenieNazwaPlikuZIP != ""):
                self.polecenieNameAfterZip = self.polecenieNazwaPliku + (".zip")
            elif (self.polecenieNazwaKATALOGU != ""):
                self.polecenieNameAfterZip = self.polecenieNazwaKATALOGU + (".zip")
            elif (self.polecenieNazwaPliku != ""):
                self.polecenieNameAfterZip = self.polecenieNazwaKATALOGU + (".zip")
            else:
                self.showCummnikate("Zapomniales wybrac pliku!",
                                    "Bez tego nie da sie uruchomic programu zip")
                czyWybranoPlik = 0
                pass

        else:
            self.polecenieNameAfterZip = "NowyZIP" + (".zip")
        #self.polecenie = self.polecenie + " " + (self.PATH)  # path to file
        if (czyWybranoPlik):
            # CZY PLIK KONCZY SIE NA ZIP ORAZ CZY TARGET NIE JEST PUSTE
            if (self.polecenieTarget != "" and self.PATH.lower().endswith(".zip")):
                czyPlikToZIP = 1
                print("self.PATH ", self.PATH)

                self.polecenie =  self.polecenieTarget + self.polecenie  #+ " " +self.commentToAdd
                self.polecenie = self.polecenie + self.polecenieIntegralTest
                if (len(self.fileToDelete) >0):
                    self.polecenie = self.polecenie + self.polecenieDeleteInZip + " " + self.PATH + " " +  self.fileToDelete #usuwanie z pliku zip
                    tmpfileToDelete = 1
            elif (self.polecenieTarget != "" and not self.PATH.endswith(".zip") and  self.polecenieNazwaPliku == "" and self.polecenieNazwaKATALOGU ==""):
                czyPlikToZIP = 0
                self.showCummnikate("ERROR!!!", " Aby operowac na plikach zip musisz wybrac plik o takim rozszerzeniu! ")
            else:
                pass

            # WYBOR OPCJI DLA PLIKOW ZIP Z CHECKBUTTONA ALE BEZ ROZWIJANEJ LISTY
            if (self.PATH.lower().endswith(".zip") and self.polecenieTarget == ""):
                czyPlikToZIP = 1
                self.polecenie = self.polecenie + self.polecenieIntegralTest #+ " "+ self.commentToAdd
                if (len(self.fileToDelete) >0):
                    self.polecenie = self.polecenie + self.polecenieDeleteInZip + " " + self.PATH + " " +  self.fileToDelete #usuwanie z pliku zip
                    tmpfileToDelete = 1
                print(self.polecenieIntegralTest, " self.polecenieIntegralTest")
            elif (self.polecenieTarget != "" and (self.ifActivetIntegralTestC() or self.ifActiveDeleteInZip())):
                self.showCummnikate("Zbyt wiele parametrw dotyczcych plikzip jednoczesnie",
                                    "Musisz wybrac czy chcesz przeprowadzic testy integralnosci i usunc wpisy czy tez wybrac opcje z rozwijanego menu")
            else:
                pass

            # OBSLUGA BLEDOW ODPOWIEDZIALNYCH ZA NIEOPDOWIEDNI DOBOR PARAMETROW
            if (not self.PATH.lower().endswith(".zip") and (
                    self.ifActivetIntegralTestC() or self.ifActiveDeleteInZip())):
                self.showCummnikate("Wybrales parametry przeznaczone dla plikow zip",
                                    "Wylacz -T, -d lub wybierz inny plik")

            if (czyPlikToZIP == 0):
                self.polecenie = zip + self.polecenieNameAfterZip  # name after zippingTH)
                self.polecenie = self.polecenie + self.polecenieCompression
                print("self.polecenieCompression ", self.polecenieCompression)
                if (self.polecenieCompression == ""):
                    self.polecenie = self.polecenie + " -6"
                    print("self.polecenieCompression ", " -6")
            else:
                self.polecenie = zip + self.polecenie
            if (tmpfileToDelete ==0):
                self.polecenie = self.polecenie + " " + (self.PATH)  # path to file

            print(self.polecenie)

            process = subprocess.Popen(self.polecenie, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT,
                                       close_fds=True)
            #try:
            if (self.commentToAdd != ""):
                print("of1")
                #xd = process.communicate(input=bytes(self.commentToAdd, 'ascii'))[0]
                outs = process.communicate(input=bytes(self.commentToAdd, 'ascii'))[0]

                print(outs.decode()) # , errs.decode())
                output = outs.decode() #, errs.decode()
                print("out", output)
                self.commentToAdd = ""
                #except:
             #   print("a")
                output=""
            try:
                output = process.stdout.read()
                print(process)
                print(output)
                self.labelOutput = self.labelOutput + "\n" + (output.decode("utf-8")) + " \n"
                self.setLabel(self.labelOutput)
                import Levenshtein
                levensteinDegree = (Levenshtein.distance(output.decode("utf-8"),
                                                         "zip warning: name not matched: " + self.inputFromDialog))
                if (output.decode(
                        "utf-8") is "zip warning: name not matched: " + self.inputFromDialog + "\n" or levensteinDegree <= 20):
                    self.showCummnikate("nie znaleziono pliku o podanej nazwie", " Sprbuj ponownie")

                pass
            except:
                print("Dodawanie komentarza do pliku")
                self.labelOutput = self.labelOutput + "\nDodano komentarz do pliku zip" + " \n"
                self.setLabel(self.labelOutput)



    def setLabel(self, string):
        self.resultLabel.set_text(string)

    def on_nameOptionRadiobutton1_toggled(self, widget, user_data=None):
        """ Handler for nameOptionRadiobutton1.toggled. """
        self.czyNazwaTaSamCOPlik = 1

        self.polecenieNameAfterZip = ""

        print(ntpath.basename(self.PATH))
        pass

    def on_nameOptionRadiobutton2_toggled(self, widget, user_data=None):
        """ Handler for nameOptionRadiobutton1.toggled. """
        self.czyNazwaTaSamCOPlik = 0

        pass

    def on_tIntegralTestCheckbutton_toggled(self, widget, user_data=None):
        """ Handler for tIntegralTestCheckbutton.toggled. """
        active = self.ifActivetIntegralTestC()
        print("self.polecenieIntegralTest", active)
        if (active):
            self.polecenieIntegralTest = " -T"
        else:
            self.polecenieIntegralTest = ""
        pass

    def on_xOptionTXTRadiobutton_toggled(self, widget, user_data=None):
        """ Handler for xOptionTXTRadiobutton.toggled. """
        pass

    # glowne przyciski wyboru trybu dzialania
    def on_toggleButton2_toggled(self, widget, user_data=None):
        self.TMPon_toggleButton2_toggled += 1
        """ Handler for toggleButton2.toggled. """
        # self.plikLubKatalog2.set_sensitive(False)
        if (self.trybToggleButton1Stan.get_active and self.TMPon_toggleButton2_toggled % 2 == 0):
            self.trybToggleButton1Stan.set_active(False)
            self.toggleButton2Stan.set_active(True)
        if (self.TMPon_toggleButton2_toggled % 2 == 1):
            self.toggleButton2Stan.set_active(False)

        if (self.toggleButton2Stan.get_active()):
            self.TargetComboboxtext.set_sensitive(False)
            self.dDeleteInZIPCheckbutton.set_sensitive(False)
            self.tIntegralTestCheckbutton.set_sensitive(False)
            self.plikLubKatalog2.set_sensitive(False)

            self.nameOptionRadiobutton1.set_sensitive(True)
            self.nameOptionRadiobutton2.set_sensitive(True)
            self.plikLubKatalog1.set_sensitive(True)
            self.plikLubKatalog.set_sensitive(True)
            self.compressionLevel.set_sensitive(True)

        pass

    def on_trybToggleButton1_toggled(self, widget, user_data=None):
        """ Handler for trybToggleButton1.toggled. """
        self.TMPon_toggleButton1_toggled += 1
        if (self.toggleButton2Stan.get_active and self.TMPon_toggleButton1_toggled % 2 == 0):
            self.toggleButton2Stan.set_active(False)
            self.trybToggleButton1Stan.set_active(True)
        if (self.TMPon_toggleButton1_toggled % 2 == 1):
            self.trybToggleButton1Stan.set_active(False)

        if (self.trybToggleButton1Stan.get_active()):
            self.TargetComboboxtext.set_sensitive(True)
            self.dDeleteInZIPCheckbutton.set_sensitive(True)
            self.tIntegralTestCheckbutton.set_sensitive(True)
            self.nameOptionRadiobutton1.set_sensitive(True)
            self.plikLubKatalog2.set_sensitive(True)

            self.nameOptionRadiobutton1.set_sensitive(False)
            self.nameOptionRadiobutton2.set_sensitive(False)
            self.plikLubKatalog1.set_sensitive(False)
            self.plikLubKatalog.set_sensitive(False)
            self.compressionLevel.set_sensitive(False)

        pass

    def guiFunctionaVisible(self):
        if (not self.toggleButton2Stan.get_active() and not self.trybToggleButton1Stan.get_active()):
            self.nameOptionRadiobutton1.set_sensitive(False)
            self.nameOptionRadiobutton2.set_sensitive(False)
            self.plikLubKatalog1.set_sensitive(False)
            self.plikLubKatalog.set_sensitive(False)
            self.compressionLevel.set_sensitive(False)
            self.TargetComboboxtext.set_sensitive(False)
            self.dDeleteInZIPCheckbutton.set_sensitive(False)
            self.tIntegralTestCheckbutton.set_sensitive(False)
            self.plikLubKatalog2.set_sensitive(False)

    def showCummnikate(self, text1, text2):
        Gtk.AboutDialog()
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text=text1,
        )
        dialog.format_secondary_text(
            text2
        )
        dialog.run()
        print("INFO dialog closed")
        dialog.destroy()

    # sprawdzenie aktywnosci przycisku -d
    def ifActiveDeleteInZip(self):
        chkbt_chrome = self.builder.get_object("dDeleteInZIPCheckbutton")
        return chkbt_chrome.get_active()

    # sprawdzenie aktywnosci przycisku -T integral test
    def ifActivetIntegralTestC(self):
        chkbt_chrome = self.builder.get_object("tIntegralTestCheckbutton")
        return chkbt_chrome.get_active()


def main():
    """ Main entry point for the program. """
    app = App()  # noqa
    return Gtk.main()


if __name__ == '__main__':
    mainret = main()
    sys.exit(mainret)
