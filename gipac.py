#!/usr/bin/env python3
import sys
import shutil


# UTF-8 ayarlarını yap
locale.getpreferredencoding = lambda: 'UTF-8'
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from PyQt5.QtWidgets import (QApplication, QWidget, QFormLayout, QLineEdit, 


def get_logo_path():
    """Logo dosyasının yolunu belirler"""
    paths = [
        "/usr/share/gipac/icons/gipaclo.png",  # Sistem geneli kurulum yolu
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "gipaclo.png"),  # Yerel dizin
        "gipaclo.png"  # Çalışma dizini
    ]
    
    # İlk bulunan dosyayı döndür
    for path in paths:
        if os.path.exists(path):
            return path
    return None

class DebCreatorApp(QWidget):
    # Lisans metnini sınıf değişkeni olarak tanımla
    LICENSE_TEXT = """
            <h2 style="color: #0077b6; text-align: center;">ALG Yazılım & Elektronik – Yazılım Lisansı</h2>
            <p><b>Lisans Veren:</b> ALG Yazılım & Elektronik<br>
            <b>Telif Hakkı Sahibi:</b> Fatih ÖNDER (CekToR)</p>

            <h3 style="color: #00b4d8;">1. Amaç</h3>
            <p>Bu lisans, GiPac - Gift Package adlı yazılımın kaynak kodunun görülebilir, ücretsiz kullanılabilir ve dağıtılabilir olmasını sağlar. Ancak yazılım üzerinde herhangi bir değişiklik, türev çalışma veya ticari kullanım kesinlikle yasaktır.</p>

            <h3 style="color: #00b4d8;">2. Haklar</h3>
            <p>Kullanıcılar:</p>
            <ul>
                <li>Yazılımı ücretsiz olarak kullanabilir.</li>
                <li>Yazılımın kaynak kodunu inceleyebilir.</li>
                <li>Yazılımı orijinal haliyle dağıtabilir.</li>
            </ul>

            <h3 style="color: #00b4d8;">3. Kısıtlamalar</h3>
            <p>Kullanıcılar:</p>
            <ul>
                <li>Yazılımın veya kaynak kodunun herhangi bir kısmını değiştiremez, uyarlayamaz veya türev eser oluşturamaz.</li>
                <li>Yazılımı ticari amaçlarla (satış, kiralama, hizmet sunumu vb.) kullanamaz.</li>
                <li>Yazılımın orijinal lisans ve telif hakkı bilgilerini kaldıramaz.</li>
            </ul>

            <h3 style="color: #00b4d8;">4. Garanti ve Sorumluluk Reddi</h3>
            <p>Yazılım "olduğu gibi" sunulmaktadır. ALG Yazılım & Elektronik ve Fatih ÖNDER (CekToR), yazılımın kullanımı sonucu doğabilecek herhangi bir zarardan sorumlu tutulamaz.</p>

            <h3 style="color: #00b4d8;">5. Geçerlilik</h3>
            <p>Bu lisans, yazılımın her kopyası için geçerlidir. Lisans koşullarına uymayan kullanıcıların lisans hakkı otomatik olarak sona erer.</p>
    """

    def __init__(self):
        super().__init__()
        # Log görüntüleyici ve iptal butonu başlatma
        self.log_text = QTextEdit()
        self.cancel_button = QPushButton('İptal')
        
        # Uygulama ikonunu ayarla
      
        
        try:
            self.initUI()
        except Exception as e:
            print(f"Başlatma hatası: {e}")
            QMessageBox.critical(None, "Kritik Hata", f"Program başlatılamadı: {e}")
            sys.exit(1)

    def create_tray_menu(self):
        """System tray menüsünü oluştur"""
        menu = QMenu()
        show_action = menu.addAction("Göster")
        show_action.triggered.connect(self.show)
        hide_action = menu.addAction("Gizle")
        hide_action.triggered.connect(self.hide)
        quit_action = menu.addAction("Çıkış")
        quit_action.triggered.connect(self.close)
        self.tray_icon.setContextMenu(menu)
        self.tray_icon.activated.connect(self.tray_icon_activated)

    def tray_icon_activated(self, reason):
        """System tray ikonu tıklandığında"""
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()

  
        self.setStyleSheet("""
            QWidget {
                font-size: 11pt;
                background-color: #1e1e1e;
                color: #ffffff;
            }
            QGroupBox {
                border: 2px solid #3a3a3a;
                border-radius: 6px;
                margin-top: 6px;
                padding-top: 10px;
                color: #00b4d8;
            }
            QPushButton {
                background-color: #0077b6;
                color: white;
                padding: 8px 15px;
                border: none;
                border-radius: 4px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #0096c7;
            }
            QPushButton:pressed {
                background-color: #023e8a;
            }
            QPushButton:disabled {
                background-color: #64748b;
            }
            QLineEdit, QPlainTextEdit, QTextEdit {
                padding: 8px;
                border: 1px solid #3a3a3a;
                border-radius: 4px;
                background-color: #2d2d2d;
                color: #ffffff;
                selection-background-color: #0077b6;
            }
            QLineEdit:focus, QPlainTextEdit:focus, QTextEdit:focus {
                border: 2px solid #0096c7;
            }
            QLabel {
                color: #e9ecef;
            }
            QComboBox {
                background-color: #2d2d2d;
                border: 1px solid #3a3a3a;
                border-radius: 4px;
                padding: 5px;
                color: white;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
                border: none;
            }
            QComboBox:on {
                border: 2px solid #0096c7;
            }
            QComboBox QAbstractItemView {
                background-color: #2d2d2d;
                color: white;
                selection-background-color: #0077b6;
            }
            QTabWidget::pane {
                border: 1px solid #3a3a3a;
                border-radius: 4px;
            }
            QTabBar::tab {
                background-color: #2d2d2d;
                color: #ffffff;
                padding: 8px 15px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #0077b6;
            }
            QTabBar::tab:hover {
                background-color: #0096c7;
            }
            QProgressBar {
                border: 1px solid #3a3a3a;
                border-radius: 4px;
                background-color: #2d2d2d;
                color: white;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #0077b6;
                border-radius: 3px;
            }
            QCheckBox {
                color: #e9ecef;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #3a3a3a;
                border-radius: 4px;
                background-color: #2d2d2d;
            }
            QCheckBox::indicator:checked {
                background-color: #0077b6;
                border: 2px solid #0096c7;
            }
            QScrollBar:vertical {
                border: none;
                background: #2d2d2d;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #0077b6;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QMessageBox {
                background-color: #1e1e1e;
                color: white;
            }
            QToolTip {
                background-color: #2d2d2d;
                color: white;
                border: 1px solid #3a3a3a;
                padding: 5px;
            }
        """)

        # Ana düzen
        main_splitter = QSplitter(Qt.Vertical)
        
        # Üst kısım (mevcut arayüz)
        top_widget = QWidget()
        main_layout = QVBoxLayout(top_widget)
        
        # Log görüntüleyici
        self.log_text.setReadOnly(True)
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #2d2d2d;
                color: #ffffff;
                font-family: 'Cascadia Code', 'Source Code Pro', monospace;
                font-size: 10pt;
                border: 1px solid #3a3a3a;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        self.log_text.setMinimumHeight(150)
        self.log_text.setMaximumHeight(200)
        
        # Mevcut arayüz elemanları
        # Tab widget oluştur
        self.tabs = QTabWidget()
        
        # Ana sekme
        main_tab = QWidget()
        main_layout_tab = QVBoxLayout()

        # Form grubu
        form_group = QGroupBox("Paket Bilgileri")
        layout = QFormLayout()

        # Paket adı
        self.packageName = QLineEdit(self)
        self.packageName.setPlaceholderText("örn: myapp")
        layout.addRow(self.create_label("Paket Adı:", "Paketin benzersiz adı"), self.packageName)

        # Sürüm
        self.version = QLineEdit(self)
        self.version.setPlaceholderText("örn: 1.0.0")
        layout.addRow(self.create_label("Sürüm:", "Paketin sürüm numarası (x.y.z)"), self.version)

        # Email
        self.email = QLineEdit(self)
        self.email.setPlaceholderText("info@algyazilim.com")
        layout.addRow(self.create_label("E-Posta:", "İletişim e-posta adresi"), self.email)

        # Website
        self.website = QLineEdit(self)
        self.website.setPlaceholderText("https://algyazilim.com")
        layout.addRow(self.create_label("Website:", "Proje web sitesi"), self.website)

        # Bakımcı
        self.author = QLineEdit(self)
        self.author.setPlaceholderText("Fatih ÖNDER (CekToR)")
        layout.addRow(self.create_label("Geliştirici:", "Paket geliştirici adı"), self.author)

        # Açıklama
        self.description = QPlainTextEdit(self)
        self.description.setPlaceholderText("Paketinizin ne yaptığını açıklayın...")
        layout.addRow(self.create_label("Açıklama:", "Paket hakkında detaylı açıklama"), self.description)

        # Bağımlılıklar
        self.dependencies = QLineEdit(self)
        self.dependencies.setPlaceholderText("örn: python3, qt5-default")
        layout.addRow(self.create_label("Bağımlılıklar:", "Virgülle ayrılmış bağımlılık listesi"), self.dependencies)

        # Dosya seçici
        file_layout = QHBoxLayout()
        self.filePath = QLineEdit(self)
        self.filePath.setPlaceholderText("Ana program dosyasını seçin...")
        self.fileButton = QPushButton("Dosya Seç", self)
        self.fileButton.clicked.connect(self.select_file)
        file_layout.addWidget(self.filePath)
        file_layout.addWidget(self.fileButton)
        layout.addRow(self.create_label("Program:", "Ana program dosyası"), file_layout)

        form_group.setLayout(layout)
        main_layout_tab.addWidget(form_group)
        
        main_tab.setLayout(main_layout_tab)
        
        # Desktop dosyası sekmesi
        desktop_tab = QWidget()
        desktop_layout = QFormLayout()

        # Masaüstü kısayol ayarları
        shortcut_group = QHBoxLayout()
        self.create_shortcut = QCheckBox("Masaüstüne Kısayol Ekle")
        self.create_shortcut.setChecked(False)
        
        self.shortcut_name = QLineEdit()
        self.shortcut_name.setPlaceholderText("Kısayol Adı (boş bırakılırsa paket adı kullanılır)")
        self.shortcut_name.setEnabled(False)
        
        self.create_shortcut.stateChanged.connect(lambda state: self.shortcut_name.setEnabled(bool(state)))
        
        shortcut_group.addWidget(self.create_shortcut)
        shortcut_group.addWidget(self.shortcut_name)
        
        desktop_layout.addRow("Kısayol:", shortcut_group)
        
        # Diğer desktop ayarları
        # Önce categories_group tanımlanmalı
        categories_group = QHBoxLayout()
        
        # Categories tanımlamaları
        categories = {
            "Erişilebilirlik": ["Utility", "Accessibility"],
            "Geliştirme": ["Development", "Building", "Debugger", "IDE"],
            "Eğitim": ["Education", "Languages", "Science", "Math"],
            "Oyunlar": ["Game", "ActionGame", "AdventureGame", "ArcadeGame", "BoardGame"],
            "Grafik": ["Graphics", "2DGraphics", "3DGraphics", "Photography", "Viewer"],
            "İnternet": ["Network", "Chat", "Feed", "FileTransfer", "WebBrowser"],
            "Ofis": ["Office", "Calendar", "Database", "Dictionary", "TextEditor"],
            "Ses ve Video": ["AudioVideo", "Audio", "Video", "Midi", "Player"],
            "Sistem": ["System", "Emulator", "FileManager", "Monitor", "Security"],
            "Yardımcı Programlar": ["Utility", "TextEditor", "Calculator", "Clock"]
        }
        
        # Ana kategori seçimi için ComboBox
        self.main_category = QComboBox()
        self.main_category.addItems(sorted(categories.keys()))
        self.main_category.setCurrentText("Yardımcı Programlar")
        self.main_category.currentTextChanged.connect(lambda text: self.update_subcategories(text, categories))
        
        # Alt kategori seçimi için ComboBox
        self.sub_category = QComboBox()
        self.sub_category.setEditable(True)
        
        # Categories gruplandırması
        categories_group.addWidget(self.main_category)
        categories_group.addWidget(self.sub_category)
        
        # İlk alt kategorileri yükle
        self.update_subcategories("Yardımcı Programlar", categories)

        # Name - TR
        name_group = QVBoxLayout()
        self.desktop_name = QLineEdit()
        self.desktop_name.setPlaceholderText("Application Name (EnCo File Encryptor)")
        self.desktop_name_tr = QLineEdit()
        self.desktop_name_tr.setPlaceholderText("Uygulama Adı (EnCo Dosya Şifreleyici)")
        name_group.addWidget(QLabel("Name:"))
        name_group.addWidget(self.desktop_name)
        name_group.addWidget(QLabel("Name[tr]:"))
        name_group.addWidget(self.desktop_name_tr)
        
        # Comment - TR
        comment_group = QVBoxLayout()
        self.desktop_comment = QLineEdit()
        self.desktop_comment.setPlaceholderText("File Encryption Application")
        self.desktop_comment_tr = QLineEdit()
        self.desktop_comment_tr.setPlaceholderText("Dosya Şifreleme Uygulaması")
        comment_group.addWidget(QLabel("Comment:"))
        comment_group.addWidget(self.desktop_comment)
        comment_group.addWidget(QLabel("Comment[tr]:"))
        comment_group.addWidget(self.desktop_comment_tr)
        
        # Type ComboBox
        self.desktop_type = QComboBox()
        self.desktop_type.addItems([
            "Application",
            "Link",
            "Directory",
            "FSDevice",
            "Service"
        ])
        self.desktop_type.setCurrentText("Application")

        # Diğer alanlar...
        self.desktop_icon = QLineEdit()
        self.desktop_icon.setPlaceholderText("/usr/share/icons/myapp.png")
        
        self.desktop_terminal = QComboBox()
        self.desktop_terminal.addItems(["false", "true"])
        self.desktop_terminal.setCurrentText("false")
        
        # Layout düzenlemesi
        desktop_layout.addRow(name_group)
        desktop_layout.addRow(comment_group)
        desktop_layout.addRow("Type:", self.desktop_type)
        desktop_layout.addRow("Categories:", categories_group)
        desktop_layout.addRow("Icon:", self.desktop_icon)
        desktop_layout.addRow("Terminal:", self.desktop_terminal)
        desktop_tab.setLayout(desktop_layout)

        # Debian dosyaları sekmesi
        debian_tab = QWidget()
        debian_layout = QFormLayout()
        
        # Changelog için yatay düzen
        changelog_layout = QHBoxLayout()
        self.changelog = QPlainTextEdit()
        self.changelog.setPlaceholderText(f"""myapp (1.0.0) stable; urgency=low

  * Initial release

 -- Maintainer <email@example.com>  {datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0300')}""")
        
        changelog_btn = QPushButton("Örnek")
        changelog_btn.clicked.connect(lambda: self.set_example_text(self.changelog, self.packageName.text(), 
                                    self.version.text(), self.author.text(), self.email.text()))
        changelog_layout.addWidget(self.changelog)
        changelog_layout.addWidget(changelog_btn)
        
        # Copyright için yatay düzen
        copyright_layout = QHBoxLayout()
        self.copyright = QPlainTextEdit()
        self.copyright.setPlaceholderText("""Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: myapp
Source: https://example.com/myapp

Files: *
Copyright: 2023 Your Name <your@email.com>
License: GPL-3.0+""")
        
        copyright_btn = QPushButton("Örnek")
        copyright_btn.clicked.connect(lambda: self.set_copyright_text(self.copyright, self.packageName.text(), 
                                    self.website.text(), self.author.text(), self.email.text()))
        copyright_layout.addWidget(self.copyright)
        copyright_layout.addWidget(copyright_btn)
        
        # Rules için yatay düzen
        rules_layout = QHBoxLayout()
        self.rules = QPlainTextEdit()
        self.rules.setPlaceholderText("""#!/usr/bin/make -f
%:
	dh $@ --with python3 --buildsystem=pybuild""")
        
        rules_btn = QPushButton("Örnek")
        rules_btn.clicked.connect(lambda: self.set_rules_text(self.rules))
        rules_layout.addWidget(self.rules)
        rules_layout.addWidget(rules_btn)
        
        debian_layout.addRow("changelog:", changelog_layout)
        debian_layout.addRow("copyright:", copyright_layout)
        debian_layout.addRow("rules:", rules_layout)
        debian_tab.setLayout(debian_layout)

        # Install dosyası sekmesi
        install_tab = QWidget()
        install_layout = QVBoxLayout()
        install_form = QFormLayout()
        self.install_entries = []
        
        default_paths = [
            ("Ana Program", "", "usr/bin/", True),
            ("İkonlar", "", "usr/share/icons/", False),
            ("Desktop Dosyası", "", "usr/share/applications/", False),
            ("Dil Dosyaları", "", "usr/share/PAKET_ADI/languages/", False),
            ("Dokümanlar", "", "usr/share/doc/PAKET_ADI/", False),
            ("Konfigürasyon", "", "etc/PAKET_ADI/", False)
        ]

        for label, src, dest, is_active in default_paths:
            row_widget = QWidget()
            row_layout = QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            
            checkbox = QCheckBox()
            checkbox.setChecked(is_active)
            
            src_edit = QLineEdit()
            src_edit.setPlaceholderText("Kaynak dosya/dizin")
            src_button = QPushButton("Gözat")
            src_button.clicked.connect(lambda checked, e=src_edit: self.select_file_or_dir(e))
            
            dest_edit = QLineEdit()
            dest_edit.setText(dest)
            
            widgets = [src_edit, src_button, dest_edit]
            for widget in widgets:
                widget.setEnabled(is_active)
            
            checkbox.stateChanged.connect(
                lambda state, w=widgets: self.update_widgets_state(w, bool(state))
            )
            
            row_layout.addWidget(checkbox)
            row_layout.addWidget(src_edit)
            row_layout.addWidget(src_button)
            row_layout.addWidget(dest_edit)
            
            row_widget.setLayout(row_layout)
            install_form.addRow(label, row_widget)
            
            self.install_entries.append((checkbox, src_edit, dest_edit))

        install_layout.addLayout(install_form)
        install_tab.setLayout(install_layout)

        # Sekmeleri ekle
        self.tabs.addTab(main_tab, "Ana Ayarlar")
        self.tabs.addTab(desktop_tab, "Desktop Dosyası")
        self.tabs.addTab(debian_tab, "Debian Dosyaları")
        self.tabs.addTab(install_tab, "Dosya Konumları")

        # Hakkında sekmesi
        about_tab = QWidget()
        about_layout = QVBoxLayout()
        
        # Logo ekle
        logo_label = QLabel()
        logo_path = get_logo_path()
        if logo_path:
            logo_pixmap = QPixmap(logo_path)
            scaled_pixmap = logo_pixmap.scaled(128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(scaled_pixmap)
            logo_label.setAlignment(Qt.AlignCenter)
            about_layout.addWidget(logo_label)
        
        about_text = QTextBrowser()
        about_text.setOpenExternalLinks(False)  # Dış linkleri açmayı devre dışı bırak
        about_text.anchorClicked.connect(self.handle_link_click)  # Sinyal bağlantısı ekle
        about_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        about_text.setHtml("""
            <div style="text-align: center;">
                <h2 style="color: #0077b6;">GiPac - Gift Package</h2>
                <h4 style="color: #0077b6;">Hediye Paketi - .deb Paket Oluşturucu</h4>
                <p>Sürüm 1.0.0</p>
            </div>
            <div style="margin: 20px;">
                <h3 style="color: #00b4d8;">Özellikler</h3>
                <ul>
                    <li>Konfigürasyon Dışa/İçe Aktarma</li>
                    <li>Debian paket (.deb) oluşturma</li>
                    <li>Desktop dosyası desteği</li>
                    <li>Debian Dosyaları</li>
                    <li>Dosya Konumları</li>
                    <li>Otomatik bağımlılık yönetimi</li>
                    <li>Kullanıcı dostu arayüz</li>
                </ul>
                
                <h3 style="color: #00b4d8;">Lisans</h3>
                <p>Bu yazılım <a href="#show_license" style="color: #00b4d8;">ALG Yazılım & Elektronik – Yazılım Lisansı</a> altında lisanslanmıştır.</p>
                
                <h3 style="color: #00b4d8;">Geliştirici</h3>
                <p>Fatih ÖNDER (CekToR)<br>
                <a style="color: #00b4d8;" href="mailto:info@algyazilim.com">info@algyazilim.com</a><br>
                <a style="color: #00b4d8;" href="https://algyazilim.com">algyazilim.com</a><br>
                <a style="color: #00b4d8;" href="https://github.com/cektor">Github</a></p>
                
                <div style="margin-top: 40px; padding: 10px; background-color: #2d2d2d; border-radius: 5px;">
                    <p style="color: #ff9800; font-style: italic; text-align: center;">
                        Bu yazılım hiçbir garanti vermemektedir. Yazılımı kullanırken oluşabilecek 
                        riskler kullanıcıya aittir.
                    </p>
                </div>
            </div>
        """)

        about_layout.addWidget(about_text)
        about_tab.setLayout(about_layout)
        
        self.tabs.addTab(about_tab, "Hakkında")
        
        main_layout.addWidget(self.tabs)
        
        # İlerleme çubuğu
        self.progress = QProgressBar(self)
        self.progress.hide()
        main_layout.addWidget(self.progress)

        # Düğmeler
        button_layout = QHBoxLayout()
        self.export_button = QPushButton('Dışa Aktar')
        self.export_button.clicked.connect(self.export_settings)
        self.export_button.setIcon(self.style().standardIcon(QStyle.SP_DialogSaveButton))
        
        self.import_button = QPushButton('İçe Aktar')
        self.import_button.clicked.connect(self.import_settings)
        self.import_button.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        
        self.helpButton = QPushButton('Yardım', self)
        self.helpButton.clicked.connect(self.show_help)
        self.helpButton.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxQuestion))
        
        self.buildButton = QPushButton('Paketi Oluştur', self)
        self.buildButton.clicked.connect(self.create_deb_package)
        self.buildButton.setIcon(self.style().standardIcon(QStyle.SP_DialogSaveButton))
        
        button_layout.addWidget(self.export_button)
        button_layout.addWidget(self.import_button)
        button_layout.addWidget(self.helpButton)
        button_layout.addWidget(self.buildButton)
        main_layout.addLayout(button_layout)

        # İlerleme çubuğu ve butonlar
        bottom_layout = QHBoxLayout()
        
        # İptal butonu
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #dc2f2f;
            }
            QPushButton:hover {
                background-color: #ef4444;
            }
            QPushButton:pressed {
                background-color: #b91c1c;
            }
        """)
        self.cancel_button.clicked.connect(self.cancel_operation)
        self.cancel_button.hide()
        
        # Progress bar düzenlemesi
        progress_layout = QVBoxLayout()
        self.progress_label = QLabel("İşlem: ")
        progress_layout.addWidget(self.progress_label)
        progress_layout.addWidget(self.progress)
        
        bottom_layout.addLayout(progress_layout)
        bottom_layout.addWidget(self.cancel_button)
        bottom_layout.addWidget(self.helpButton)
        bottom_layout.addWidget(self.buildButton)
        
        main_layout.addLayout(bottom_layout)



        self.setLayout(final_layout)

    def create_label(self, text, tooltip):
        label = QLabel(text)
        label.setToolTip(tooltip)
        return label

    def select_file(self):
        """Ana program dosyası seçici"""
        fname, _ = QFileDialog.getOpenFileName(
            self, 
            'Program Dosyası Seç', 
            '', 
            'Tüm Çalıştırılabilir Dosyalar (*.py *.exe *.AppImage *.bin *.sh);;'
            'Python Dosyaları (*.py);;'
            'Linux Çalıştırılabilir (*.AppImage *.bin *.sh);;'
            'Windows Çalıştırılabilir (*.exe);;'
            'Tüm Dosyalar (*)'
        )
        if fname:
            self.filePath.setText(fname)

    def show_help(self):
        """Özelleştirilmiş yardım dialogu"""
        help_dialog = QDialog(self)
        help_dialog.setWindowTitle("GiPac - Gift Package")
        help_dialog.setMinimumSize(600, 400)
        
        layout = QVBoxLayout(help_dialog)
        
        help_text = QTextEdit()
        help_text.setReadOnly(True)
        help_text.setHtml("""
<style>
    h2 { color: #4CAF50; margin-top: 10px; }
    h3 { color: #2196F3; margin-left: 10px; }
    p { margin-left: 20px; }
    .warning { color: #f44336; }
    .note { color: #ff9800; }
</style>

<h2>1. Ana Ayarlar</h2>
<h3>Paket Adı:</h3>
<p>• Küçük harfler ve tire (-) kullanın<br>
• Örnek: my-application</p>

<h3>Sürüm ve Bakımcı:</h3>
<p>• Sürüm: 1.0.0 formatında<br>
• Bakımcı: Ad Soyad &lt;email@adres.com&gt;</p>

<h2>2. Desktop Dosyası</h2>
<p>• Name: Görünen ad<br>
• Categories: Uygulama türü<br>
• Icon: Simge yolu</p>

<h2>3. Debian Dosyaları</h2>
<p>• Changelog: Sürüm değişiklikleri<br>
• Copyright: Lisans bilgileri</p>

<h2>4. Dosya Konumları</h2>
<p>• Dosyaların sisteme kurulum yerleri<br>
• PAKET_ADI otomatik değiştirilir</p>

<p class="warning">Önemli: Paket adı ve sürüm Debian standartlarına uygun olmalı!</p>

<p class="note">Detaylı bilgi:<br>
<a href="https://www.debian.org/doc/debian-policy/">Debian Paketleme Kılavuzu</a></p>
""")
        
        close_button = QPushButton("Kapat")
        close_button.clicked.connect(help_dialog.close)
        
        layout.addWidget(help_text)
        layout.addWidget(close_button)
        
        help_dialog.exec_()

    def show_license(self):
        """Lisans popup'ını göster"""
        license_dialog = QDialog(self)
        license_dialog.setWindowTitle("ALG Yazılım & Elektronik – Yazılım Lisansı")
        license_dialog.setMinimumSize(600, 500)
        
        layout = QVBoxLayout(license_dialog)
        
        text = QTextBrowser()
        text.setOpenExternalLinks(False)
        text.setHtml(self.LICENSE_TEXT)
        
        close_button = QPushButton("Kapat")
        close_button.clicked.connect(license_dialog.close)
        
        layout.addWidget(text)
        layout.addWidget(close_button)
        
        license_dialog.exec_()

    def handle_link_click(self, url):
        """Link tıklamalarını yönet"""
        if url.toString() == "#show_license":  # # işareti eklendi
            self.show_license()
        else:
            QDesktopServices.openUrl(url)

    def select_directory(self, edit_widget):
        """Dizin seçme dialogu"""
        directory = QFileDialog.getExistingDirectory(self, "Dizin Seç", "",
                                                   QFileDialog.ShowDirsOnly)
        if directory:
            edit_widget.setText(directory)

    def select_file_or_dir(self, edit_widget):
        """Geliştirilmiş dosya/dizin seçici"""
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)  # Çoklu dosya seçimine izin ver
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        dialog.setViewMode(QFileDialog.Detail)
        
        # Dosya filtreleri
        dialog.setNameFilter("Tüm Dosyalar (*);;Python Dosyaları (*.py);;Resim Dosyaları (*.png *.jpg *.svg);;Metin Dosyaları (*.txt)")
        
        # Dizin seçimi için buton ekle
        dirs_button = dialog.findChild(QPushButton, "dirButton")
        if not dirs_button:
            dirs_button = QPushButton("Dizin Seç", dialog)
            dirs_button.clicked.connect(lambda: dialog.setFileMode(QFileDialog.Directory))
            dialog.layout().addWidget(dirs_button)
        
        if dialog.exec_() == QFileDialog.Accepted:
            selected = dialog.selectedFiles()
            if selected:
                # Çoklu seçimleri ; ile birleştir
                edit_widget.setText(";".join(selected))
                self.log(f"Seçilen öğeler: {len(selected)}", "info")

    def update_widgets_state(self, widgets, state):
        """Widget'ların durumunu güncelle"""
        for widget in widgets:
            widget.setEnabled(state)

    def log(self, message, level="info"):
        """Log mesajı ekle"""
        colors = {
            "info": "#ffffff",
            "success": "#4CAF50",
            "error": "#f44336",
            "warning": "#ff9800"
        }
        color = colors.get(level, "#ffffff")
        self.log_text.append(f'<span style="color: {color}">[{level.upper()}] {message}</span>')
        self.log_text.moveCursor(QTextCursor.End)


    def create_deb_package(self):
        try:
            # Önce çıktı dizinini seç
            output_dir = QFileDialog.getExistingDirectory(
                self,
                "Paket Nereye Kaydedilsin?",
                os.path.expanduser("~"),  # Varsayılan olarak home dizini
                QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
            )
            
            if not output_dir:  # Kullanıcı iptal ettiyse
                return
                
            self.buildButton.setEnabled(False)
            self.cancel_button.show()
            self.progress.show()
            self.progress.setValue(0)
            
            self.log("Paket oluşturma işlemi başlatılıyor...", "info")
            
            package_name = self.packageName.text().strip().replace(" ", "-").lower()
            version = self.version.text().strip()
            author_name = self.author.text().strip()
            author_email = self.email.text().strip()
            author = f"{author_name} <{author_email}>"  # Birleştirme burada yapılıyor
            description = self.description.toPlainText().strip()
            dependencies = self.dependencies.text().strip()
            file_path = self.filePath.text().strip()
            
            # Zorunlu alanları kontrol etme
            if not all([package_name, version, author, description, file_path]):
                QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")
                self.progress.hide()
                return

            # Önce temp dizinini ve alt dizinleri oluştur
            temp_dir = f"temp_{package_name}"
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

            # Tüm gerekli dizinleri oluştur
            os.makedirs(f"{temp_dir}/DEBIAN", exist_ok=True)
            os.makedirs(f"{temp_dir}/usr/bin", exist_ok=True)
            os.makedirs(f"{temp_dir}/usr/share/applications", exist_ok=True)
            os.makedirs(f"{temp_dir}/usr/share/icons", exist_ok=True)

            self.progress.setValue(20)

            # Bağımlılıkları hazırla - sadece kullanıcının girdiklerini kullan
            if dependencies:
                deps = [d.strip() for d in dependencies.split(",") if d.strip()]
                dependencies = ", ".join(deps) + "\n"
            else:
                dependencies = "python3\n"  # En azından python3 bağımlılığı olsun

            # Control dosyasını yaz
            # Categories'den Section'ı belirle
            section_mapping = {
                "Utility": "utils",
                "Development": "devel",
                "Game": "games",
                "Graphics": "graphics",
                "Network": "net",
                "Office": "text",
                "AudioVideo": "sound",
                "System": "admin",
                "Education": "education"
            }
            
            main_category = self.sub_category.currentText().split(";")[0]
            section = section_mapping.get(main_category, "utils")
            
            control_content = f"""Package: {package_name}
Version: {version}
Section: {section}
Priority: optional
Architecture: all
Maintainer: {author}
Homepage: {self.website.text().strip()}
Description: {description}
Depends: {dependencies}"""

            # Control dosyasını yaz
            with open(f"{temp_dir}/DEBIAN/control", "w", encoding='utf-8', newline='\n') as f:
                f.write(control_content)

            # Desktop dosyası oluştur
            desktop_content = f"""[Desktop Entry]
Name={self.desktop_name.text() or package_name}
Name[tr]={self.desktop_name_tr.text()}
Comment={self.desktop_comment.text() or description}
Comment[tr]={self.desktop_comment_tr.text()}
Exec=/usr/bin/{package_name}
Terminal={self.desktop_terminal.currentText()}
Type={self.desktop_type.currentText()}
Icon={self.desktop_icon.text() or f'/usr/share/icons/{package_name}.png'}
Categories={self.sub_category.currentText()};
"""
            # Changelog içeriğini de güncelle
            changelog_content = f"""{package_name} ({version}) stable; urgency=low

  * Initial release

 -- {author}  {datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0300')}"""
            
            with open(f"{temp_dir}/DEBIAN/changelog", "w", encoding='utf-8', newline='\n') as f:
                f.write(changelog_content)
                
            with open(f"{temp_dir}/DEBIAN/copyright", "w", encoding='utf-8', newline='\n') as f:
                f.write(self.copyright.toPlainText())
                
            with open(f"{temp_dir}/DEBIAN/rules", "w", encoding='utf-8', newline='\n') as f:
                f.write(self.rules.toPlainText())
            os.chmod(f"{temp_dir}/DEBIAN/rules", 0o755)

            # Desktop dosyasını oluştur ve yaz
            with open(f"{temp_dir}/usr/share/applications/{package_name}.desktop", "w", encoding='utf-8', newline='\n') as f:
                f.write(desktop_content)

            # Program dosyasını kopyala
            dest_path = f"{temp_dir}/usr/bin/{package_name}"
            try:
                # Önce dosya türünü kontrol et
                if file_path.endswith('.py'):
                    # Python dosyası için UTF-8 encoding kullan
                    try:
                        with open(file_path, 'r', encoding='utf-8') as source:
                            content = source.read()
                        with open(dest_path, 'w', encoding='utf-8', newline='\n') as dest:
                            dest.write("#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n")
                            dest.write(content)
                    except UnicodeDecodeError:
                        # UTF-8 ile açılamazsa binary olarak kopyala
                        shutil.copy2(file_path, dest_path)
                        with open(dest_path, 'r+b') as f:
                            content = f.read()
                            f.seek(0)
                            f.write(b"#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n" + content)
                else:
                    # Diğer tüm dosyalar için binary kopyalama yap
                    shutil.copy2(file_path, dest_path)
            
                # Çalıştırma izni ver
                os.chmod(dest_path, 0o755)
                self.log(f"Program dosyası kopyalandı: {dest_path}", "success")

            except Exception as e:
                self.log(f"Dosya kopyalama hatası: {str(e)}", "error")
                raise

            self.progress.setValue(80)

            # Install dosyalarını kopyala - sadece aktif olanları
            for checkbox, src_edit, dest_edit in self.install_entries:
                if checkbox.isChecked():
                    src_paths = src_edit.text().strip().split(";")  # ; ile ayrılmış yolları böl
                    dest_base = dest_edit.text().strip()
                    
                    for src_path in src_paths:
                        if src_path and dest_base:
                            # PAKET_ADI placeholder'ını gerçek paket adıyla değiştir
                            dest_base = dest_base.replace("PAKET_ADI", package_name)
                            dest_path = f"{temp_dir}/{dest_base}"
                            
                            # Hedef dizini oluştur
                            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                            
                            try:
                                if os.path.isdir(src_path):
                                    # Dizin kopyalama
                                    shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
                                else:
                                    # Dosya kopyalama
                                    shutil.copy2(src_path, dest_path)
                            except Exception as e:
                                print(f"Kopyalama hatası: {e}")

            # Masaüstü kısayolu oluştur
            if self.create_shortcut.isChecked():
                # Kullanıcının home dizinini al
                home_dir = os.path.expanduser("~")
                desktop_dir = os.path.join(home_dir, "Desktop")
                # Eğer Desktop klasörü yoksa Masaüstü'nü dene (Türkçe sistemler için)
                if not os.path.exists(desktop_dir):
                    desktop_dir = os.path.join(home_dir, "Masaüstü")
                
                if os.path.exists(desktop_dir):
                    shortcut_name = self.shortcut_name.text().strip() or package_name
                    desktop_shortcut_path = os.path.join(desktop_dir, f"{shortcut_name}.desktop")
                    
                    shortcut_content = f"""[Desktop Entry]
Name={shortcut_name}
Name[tr]={self.desktop_name_tr.text() or shortcut_name}
Comment={self.desktop_comment.text() or description}
Comment[tr]={self.desktop_comment_tr.text()}
Exec=/usr/bin/{package_name}
Terminal={self.desktop_terminal.currentText()}
Type=Application
Icon={self.desktop_icon.text() or f'/usr/share/icons/{package_name}.png'}
Categories={self.sub_category.currentText()};
"""
                    # Masaüstüne kısayol dosyası oluştur
                    with open(desktop_shortcut_path, "w", newline='\n') as f:
                        f.write(shortcut_content)
                    
                    # Kısayol dosyasına çalıştırma izni ver
                    os.chmod(desktop_shortcut_path, 0o755)
                    
                    self.log(f"Masaüstü kısayolu oluşturuldu: {desktop_shortcut_path}", "success")
                else:
                    self.log("Masaüstü dizini bulunamadı!", "warning")

            # Paketi oluştur - seçilen dizinde
            output_deb = os.path.join(output_dir, f"{package_name}_{version}_all.deb")
            result = subprocess.run(
                ["dpkg-deb", "--build", "--root-owner-group", temp_dir, output_deb],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                raise Exception(f"dpkg-deb hatası: {result.stderr}")

            # Temizlik
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

            self.progress.setValue(100)
            QMessageBox.information(
                self, 
                "Başarılı",
                f"Paket başarıyla oluşturuldu: {output_deb}\n"
                f"Konum: {os.path.abspath(output_deb)}"
            )
            self.log(f"Paket başarıyla oluşturuldu: {output_deb}", "success")

        except Exception as e:
            self.log(f"Hata oluştu: {str(e)}", "error")
            QMessageBox.critical(self, "Hata", f"Paket oluşturulurken hata: {str(e)}")
        finally:
            self.cleanup()

    # Alt kategorileri güncelleme metodu
    def update_subcategories(self, main_category, categories_dict):
        self.sub_category.clear()
        if main_category in categories_dict:
            self.sub_category.addItems(categories_dict[main_category])
            if categories_dict[main_category]:
                self.sub_category.setCurrentText(categories_dict[main_category][0])

    def closeEvent(self, event):
        """Uygulama kapatılırken system tray'i temizle"""
        if hasattr(self, 'tray_icon'):
            self.tray_icon.hide()
        event.accept()

    def open_link(self, url):
        """Harici linkleri aç"""
        QDesktopServices.openUrl(url)

    # Yeni metodları ekle
    def set_example_text(self, textbox, package_name, version, author, email):
        """Changelog için örnek metin"""
        if not package_name:
            package_name = "myapp"
        if not version:
            version = "1.0.0"
        if not author or not email:
            maintainer = "Maintainer <email@example.com>"
        else:
            maintainer = f"{author} <{email}>"
            
        text = f"""{package_name} ({version}) stable; urgency=low

  * Initial release

 -- {maintainer}  {datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0300')}"""
        textbox.setPlainText(text)

    def set_copyright_text(self, textbox, package_name, website, author, email):
        """Copyright için örnek metin"""
        if not package_name:
            package_name = "myapp"
        if not website:
            website = "https://example.com/myapp"
        if not author or not email:
            copyright_holder = "Your Name <your@email.com>"
        else:
            copyright_holder = f"{author} <{email}>"
            
        text = f"""Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: {package_name}
Source: {website}

Files: *
Copyright: {datetime.now().year} {copyright_holder}
License: GPL-3.0+"""
        textbox.setPlainText(text)

    def set_rules_text(self, textbox):
        """Rules için örnek metin"""
        text = """#!/usr/bin/make -f
%:
	dh $@ --with python3 --buildsystem=pybuild"""
        textbox.setPlainText(text)

    def export_settings(self):
        """Tüm ayarları JSON dosyasına kaydet"""
        try:
            settings = {
                'package_name': self.packageName.text(),
                'version': self.version.text(),
                'email': self.email.text(),
                'website': self.website.text(),
                'author': self.author.text(),
                'description': self.description.toPlainText(),
                'dependencies': self.dependencies.text(),
                'file_path': self.filePath.text(),
                'desktop': {
                    'create_shortcut': self.create_shortcut.isChecked(),
                    'shortcut_name': self.shortcut_name.text(),
                    'name': self.desktop_name.text(),
                    'name_tr': self.desktop_name_tr.text(),
                    'comment': self.desktop_comment.text(),
                    'comment_tr': self.desktop_comment_tr.text(),
                    'type': self.desktop_type.currentText(),
                    'icon': self.desktop_icon.text(),
                    'terminal': self.desktop_terminal.currentText(),
                    'category': self.main_category.currentText(),
                    'subcategory': self.sub_category.currentText()
                },
                'debian': {
                    'changelog': self.changelog.toPlainText(),
                    'copyright': self.copyright.toPlainText(),
                    'rules': self.rules.toPlainText()
                },
                'install_entries': [
                    {
                        'enabled': checkbox.isChecked(),
                        'source': src.text(),
                        'destination': dest.text()
                    }
                    for checkbox, src, dest in self.install_entries
                ]
            }
            
            file_name, _ = QFileDialog.getSaveFileName(
                self,
                "Ayarları Kaydet",
                os.path.expanduser("~"),
                "GiPac Ayarları (*.gipac);;Tüm Dosyalar (*)"
            )
            
            if file_name:
                if not file_name.endswith('.gipac'):
                    file_name += '.gipac'
                with open(file_name, 'w', encoding='utf-8', newline='\n') as f:
                    json.dump(settings, f, ensure_ascii=False, indent=4)
                self.log(f"Ayarlar başarıyla dışa aktarıldı: {file_name}", "success")
        except Exception as e:
            self.log(f"Dışa aktarma hatası: {str(e)}", "error")
            QMessageBox.critical(self, "Hata", f"Ayarlar dışa aktarılırken hata oluştu: {str(e)}")

    def import_settings(self):
        """JSON dosyasından ayarları yükle"""
        try:
            file_name, _ = QFileDialog.getOpenFileName(
                self,
                "Ayarları Yükle",
                os.path.expanduser("~"),
                "GiPac Ayarları (*.gipac);;Tüm Dosyalar (*)"
            )
            
            if file_name:
                with open(file_name, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                
                # Ana ayarlar
                self.packageName.setText(settings.get('package_name', ''))
                self.version.setText(settings.get('version', ''))
                self.email.setText(settings.get('email', ''))
                self.website.setText(settings.get('website', ''))
                self.author.setText(settings.get('author', ''))
                self.description.setPlainText(settings.get('description', ''))
                self.dependencies.setText(settings.get('dependencies', ''))
                self.filePath.setText(settings.get('file_path', ''))
                                
                              
                # Install entries
                install_entries = settings.get('install_entries', [])
                for entry, (checkbox, src, dest) in zip(install_entries, self.install_entries):
                    checkbox.setChecked(entry.get('enabled', False))
                    src.setText(entry.get('source', ''))
                    dest.setText(entry.get('destination', ''))
                
                self.log(f"Ayarlar başarıyla içe aktarıldı: {file_name}", "success")
        except Exception as e:
            self.log(f"İçe aktarma hatası: {str(e)}", "error")
            QMessageBox.critical(self, "Hata", f"Ayarlar içe aktarılırken hata oluştu: {str(e)}")

# Uygulamanın çalıştırılması
if __name__ == '__main__':
    try:
    except Exception as e:
        print(f"Program çalıştırma hatası: {e}")
        QMessageBox.critical(None, "Kritik Hata", str(e))
