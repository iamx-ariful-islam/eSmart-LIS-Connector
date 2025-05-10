# eSmart LIS Connector

### **A Python3 gui-based _lis connector_ using Tkinter GUI**

[Tkinter](https://en.wikipedia.org/wiki/Tkinter) is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's defacto standard GUI.
<br/>

**eSmart LIS Connector** is a communication bridge between medical pathology analyzers and LIS servers. It supports both serial and network connections in unidirectional or bidirectional modes using ASTM or HL7 protocols. The connector receives raw byte data, parses it and sends it to a local or API-based server/database. It is capable of handling multiple analyzers simultaneously, ensuring seamless and real-time data communication.
<br/>

**`eSmart LIS Connector` supports serial and network communication protocols, simulates and exchanges data using ASTM and HL7 formats and is compatible with `all types of pathology analyzers`.**


## Task Descriptions
This project is fully customizable and dynamic. It is designed to build a Python and Tkinter-based desktop application that connects directly to any type of analyzer via network or serial port communication, receives data, parses the results and sends them to an api server or database. You can add pathologist information, doctor information with signature. Everyday create report folder with file name is current date and printed result stored as pdf. Already `35+ Company or Category Analyzers` use this. Here are some special features added.

* **Theme Switch:** Toggle between Dark and Light modes for better visibility.
* **Running Time Clock:** Displays the application's digital uptime clock.
* **Log File Generation:** Saves terminal logs as .txt files in the output folder for future debugging or reference.
* **Live Data from Analyzers:** Displays parsed data received from multiple analyzers in real time.
* **Multi-Target Data Sync:** Sends parsed data to multiple databases or API servers simultaneously.


## Task Requirements & Testing Environments
This project was developed using the latest operating systems, software and tools.

* **Operating System :** Windows11, Kali Linux
* **Software :** Python3.12 and Visual Studio Code
* **System Type :** 32-bit and 64-bit
* **Analyzer Company :** Sysmex, ExcBio, Hermes, Genrui, Dymind, Rayto, ZECEN, Arrows, GeteIn, Arkray, Drawray, Erba, Mindray, ZyBio, Randox, Snibe, Cobas, Beckman Coulter, Indiko etc as tested.
* **Connection :** Multiple analyzers connect at a time.
* **Mode :** Single/Bidirectional/Unidirectional.
* **Protocol :** ASTM/HL7 (TCP/IP, COM).
* **Options :** 3/5/6 parts or others.
* **Types :** Hematology, Auto-Biochemistry, Auto-Horme/Immunology or any type of analyzers.
* **Database :** Multiple(SQLite3, MySQL, Oracle, MongoDB etc) database connection at a time.


## Installation
First [download](https://www.python.org/downloads/), install and configure [python](https://www.python.org/doc/). Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install on.

* Windows installation
* Kali linux installation
---


## The project is structured as follows:

```bash
esmart-lis-connector/
├── assets/
├── components/
├── database/
├── logs/
├── output/
├── screenshots/
|   ├── welcome.png
|   ├── ...
├── doc_note.txt
├── MainWindow.py        # main file
├── notes.txt            # how to use
├── README.md            # project description
├── requirements.txt     # lists of all python libraries
└── LICENSE              # license file
```


## Clone the Repository

```bash
git clone https://github.com/iam-ariful-islam/esmart-lis-connector.git
```


## Notes
The `requirements.txt` file, lists of all the Python libraries that my "**_esmart lis connector system_**" depends on and installs those packages from the file and for better use, configure the system by looking at the `notes.txt` name file:

```
pip install -r requirements.txt
```

### **or**

```
sudo pip install -r requirements.txt
```


## Project screenshots
**Welcome Page**<br/>
<img alt="welcome" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/welcome.png" />

**Main Window**<br/>
<img alt="main" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/main.png" />

**Add Information**<br/>
<img alt="add_info" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/add_info.png" />

**System Configure**<br/>
<img alt="system_configure" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/system_configure.png" />

**Parameters Setup**<br/>
<img alt="setup_parameters" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/setup_parameters.png" />

**Analyzers Setup**<br/>
<img alt="setup_analyzers" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/setup_analyzers.png" />

**Setup Extra Database**<br/>
<img alt="setup_extra_database" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/setup_extra_database.png" />

**API Server Setup**<br/>
<img alt="setup_api_server" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/setup_api_server.png" />

**Code Snapshot**<br/>
<img alt="code_snapshot" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/code_snapshot.png" />

**Output-Data is sent to a MySQL server | Old Version | Windows 7**<br/>
<img alt="data_send" src="https://github.com/iam-ariful-islam/eSmart-LIS-Connector/blob/main/screenshots/data_send.png" />


## Code Explanation
Data received from analyzers is parsed according to the protocol, queued for processing and then inserted into the appropriate database or forwarded to an API server. The GUI is designed with ease-of-use and diagnostics in mind, making the tool both powerful and accessible.


## Acknowledgments
* **Python & Tkinter:** For enabling a robust, platform-independent GUI.
* **PySerial & Socket Libraries:** For seamless serial and network communication.
* **ASTM/HL7 Community:** For providing documentation and open protocol references.
* **Stack Overflow & GitHub:** For helpful discussions, examples and troubleshooting support.
* **Open Source Community:** For inspiration, libraries and continuous contributions to healthcare integration tools.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

* Fork the repository.
* Create a new branch (git checkout -b feature-name).
* Commit your changes (git commit -am 'Add new feature').
* Push to your branch (git push origin feature-name).
* Create a new Pull Request.

Please make sure to update tests as appropriate.


## For more or connect with me
<p align='center'>
  <a href="https://github.com/iam-ariful-islam"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://twitter.com/am_ariful_islam"><img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://bd.linkedin.com/in/im-ariful-islam"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.facebook.com/jonakisoft.net/"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>


## License
The [MIT](https://choosealicense.com/licenses/mit/) License (MIT)