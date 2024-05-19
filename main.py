import tkinter as tk
import requests

def create_curl():
    service_id = eval(ent1.get())
    document_id = eval(ent2.get())
    paraphrase = txt.get(1.0, tk.END)
    headers = {
        'AUTOFAQ-User-Token':'',
        'Accept':'application/json, text/plain, */*',
        'Content-Type':'application/json'}
    data = {
        "service_id": service_id,
        "document_id": document_id,
        "author": "Буш",
        "paraphrase": paraphrase 
    }
    r = requests.post('https://127.0.0.1:4000', data=data, headers=headers)
    f = open('main.json', 'wb')
    f.write(r.content)
    f.close()

win = tk.Tk()
win.title('first')
tk.Label(win, borderwidth=5, relief="raised", height=9, width=15, text='Message\n text').grid(row=0, column=0, stick='nswe')
txt = tk.Text(win, borderwidth=5, relief="raised"); txt.grid(row=0, column=1, stick='nswe')
tk.Button(win, text='PUSH', borderwidth=5, relief="raised", width=15, command=create_curl).grid(row=0, column=2, stick='nswe')
tk.Label(win, borderwidth=5, relief="raised", height=2, width=15, text='service_id:').grid(row=1, column=0, stick='nswe')
ent1 = tk.Entry(win, borderwidth=5, relief="raised"); ent1.grid(row=1, column=1, stick='nswe')
tk.Label(win, borderwidth=5, relief="raised", height=2, width=15, text='document_id:').grid(row=2, column=0, stick='nswe')
ent2 = tk.Entry(win, borderwidth=5, relief="raised"); ent2.grid(row=2, column=1, stick='nswe')
win.mainloop()