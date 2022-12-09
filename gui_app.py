from tkinter import *
from tkinter import messagebox
from scrapy.utils import project
from scrapy import spiderloader
from tkinter import filedialog
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
import threading

# start_inp = "04/05/2022"
#-------------------------------------------------------------------
def get_browse_btn():
    global folder_path
    folder_path =  filedialog.askdirectory() 
    folder_path_entry.delete(0, END)
    folder_path_entry.insert(0, folder_path)
    return folder_path

def get_execute_btn():
    if dataset_entry.get() == '':      #or chosen_feed not in ['CSV']:
        messagebox.showerror('Error', 'All fields are mandatory')
        return
    
    try:
        feed_uri = f"file:////{folder_path}/{dataset_entry.get()}.csv"  #{chosen_feed}
    except:
        messagebox.showerror('Error', 'All entries are required')
        
    settings = project.get_project_settings()
    settings.set('FEED_URI',feed_uri)
    settings.set('FEED_FORMAT', 'csv')
    
    configure_logging()
    runner = CrawlerRunner(settings)
    runner.crawl('restipa') #change to our own spider to run
    reactor.run(installSignalHandlers=False)
    
def start_execute_thread(event):
    global execute_thread
    execute_thread = threading.Thread(target=get_execute_btn, daemon=True)
    execute_thread.start()
    app.after(10, check_execute_thread)
    
def check_execute_thread():
    if execute_thread.is_alive():
        app.after(10, check_execute_thread)
    
app= Tk()

#---input the start date 
start_input_label = Label(app, text='Chose Input Date')
start_input_label.grid(row=0, column=0, sticky=W, padx=10,pady=10)

start_input_text= StringVar(app)
start_input_entry = Entry(app, textvariable=start_input_text, width=12)
start_input_entry.grid(row=0, column=1, pady=12, padx=20)

print(start_input_text)

#------------------------------------------------------------
# path entry 
folder_path_text= StringVar(app)
folder_path_entry = Entry(app, textvariable=folder_path_text)
folder_path_entry.grid(row=4, column=0, pady=12, padx=12)

# dataset entry
dataset_text= StringVar(app)
dataset_entry = Entry(app, textvariable=dataset_text, width=12)
dataset_entry.grid(row=4, column=1, pady=12, padx=20)

browse_btn = Button(app, text='Browse', command=get_browse_btn)
browse_btn.grid(row=4, column=2)

execute_btn = Button(app, text='Execute', command=lambda: start_execute_thread(None))
execute_btn.grid(row=5, column=0, columnspan=3)

app.title('Rest in peace')
app.geometry('350x200')
app.resizable(False, False)
app.mainloop()






# def get_chosen_spider(value):
#     global chosen_spider
#     chosen_spider = value
#     return chosen_spider
    
# def get_chosen_feed(value):
#     global chosen_feed
#     chosen_feed = value
#     return chosen_feed
    
# def get_spider():
#     settings = project.get_project_settings()
#     spider_loader = spiderloader.SpiderLoader.from_settings(settings)
#     return spider_loader.list()




#spider list 
# spider_label = Label(app, text='Chose A Spider')
# spider_label.grid(row=0, column=0, sticky=W, padx=10,pady=10)

# spider_text = StringVar(app)
# spider_text.set('restipa')
# spiders = 'restipa'  #[spider for spider in get_spider()]

# spiders_dropdown = OptionMenu(app, spider_text, *spiders, command=get_chosen_spider)
# spiders_dropdown.grid(row=0, column=1, columnspan=2)

# ---feed export 
# feed_label = Label(app, text='Chose A feed')
# feed_label.grid(row=1, column=0, sticky=W, padx=10,pady=10)

# feed_text = StringVar(app)
# feed_text.set('Chose a feed')
# feeds = ['CSV']

# feeds_dropdown = OptionMenu(app, feed_text, *feeds, command=get_chosen_feed)
# feeds_dropdown.grid(row=1, column=1, columnspan=2)





