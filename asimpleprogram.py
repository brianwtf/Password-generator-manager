import random as r,string as s,tkinter as t,os as o,subprocess as sp
from tkinter import messagebox as m,simpledialog as d
from cryptography.fernet import Fernet as F
A="encrypted_password.key";B=None
print("By Brian" * 1000)
def a(l=20):return''.join(r.choice(s.ascii_letters+s.digits+s.punctuation)for _ in range(l))
def b(S,P):f=f"{S}.txt";open(f,'w').write(f"Generated password for {S}: {P}\n");c(f);m.showinfo("Success",f"Password saved to {f}")
def c(f):o.system(f'attrib +h "{f}"')if o.name=='nt'else o.rename(f,f".{f}")
def d_():
    S=d.askstring("Input","Enter the service name (e.g., Discord, Gmail):")
    if not S:m.showerror("Error","Please enter a valid service name.");return
    P=a();b(S,P);e()
def f(S):
    F=f"{S}.txt";H=f".{F}"
    if o.path.exists(H):F=H
    if o.path.exists(F):
        if o.name=='nt':o.startfile(F)
        elif o.name=='posix':sp.Popen(['open',F])
        else:sp.Popen(['xdg-open',F])
    else:m.showerror("Error",f"No password saved for {S}.")
def e():
    if not g():return
    [w.destroy()for w in pl.winfo_children()]
    L=[x for x in o.listdir()if x.endswith('.txt')or x.startswith('.')]
    S=[x[1:]if x.startswith('.')else x[:-4]for x in L]
    if not S:m.showinfo("No saved passwords","No passwords saved yet.");return
    for s_ in S:
        p=t.Button(pl,text=s_,width=50,height=2,command=lambda s=s_:f(s),bg=Q[K["mode"]]["btn_bg"],fg=Q[K["mode"]]["fg"],activebackground=Q[K["mode"]]["btn_hover"],activeforeground=Q[K["mode"]]["fg"],font=("Arial",10),bd=0,relief=t.FLAT)
        p.bind("<Enter>",z);p.bind("<Leave>",y);p.pack(pady=5)
def g():
    global B
    if B is None:
        B=n()
        if B is None:
            B=d.askstring("Create Password","Set a password to access saved passwords:")
            if B:h(B);m.showinfo("Password Set","Password has been set successfully!")
            else:m.showerror("Error","Password cannot be empty.");return False
    return d.askstring("Enter Password","Enter the password to view saved passwords:",show="*")==B or m.showerror("Incorrect Password","The password you entered is incorrect.")and False
def h(p):
    k=F.generate_key()
    c=F(k)
    x=c.encrypt(p.encode())
    open(A,'wb').write(k+b'\n'+x)
def n():
    if not o.path.exists(A):return None
    with open(A,'rb')as f:D=f.read();k,x=D.split(b'\n',1)
    return F(k).decrypt(x).decode()
R=t.Tk()
R.title("Password manager | By Brian")
R.geometry("600x600")
K={"mode":"dark"}
Q={"dark":{"bg":"#2E2E2E","fg":"#FFFFFF","btn_bg":"#444444","btn_hover":"#555555"},"light":{"bg":"#F0F0F0","fg":"#000000","btn_bg":"#DDDDDD","btn_hover":"#CCCCCC"}}
def x():
    T=Q[K["mode"]]
    R.configure(bg=T["bg"])
    pl.configure(bg=T["bg"])
    for w in R.winfo_children():
        if isinstance(w,t.Button):w.configure(bg=T["btn_bg"],fg=T["fg"],activebackground=T["btn_hover"],activeforeground=T["fg"])
    for w in pl.winfo_children():
        if isinstance(w,t.Button):w.configure(bg=T["btn_bg"],fg=T["fg"],activebackground=T["btn_hover"],activeforeground=T["fg"])
def z(e):e.widget['background']=Q[K["mode"]]["btn_hover"]
def y(e):e.widget['background']=Q[K["mode"]]["btn_bg"]
def j(m,s,C):
    T=Q[K["mode"]]
    B=t.Button(m,text=s,command=C,font=("Arial",12),bg=T["btn_bg"],fg=T["fg"],activebackground=T["btn_hover"],activeforeground=T["fg"],bd=0,relief=t.FLAT,padx=10,pady=5)
    B.bind("<Enter>",z)
    B.bind("<Leave>",y)
    return B
def i():K["mode"]="light"if K["mode"]=="dark"else"dark";x()
pl=t.Frame(R);pl.pack(pady=20)
j(R,"Generate & Save Password",d_).pack(pady=10)
j(R,"View Saved Passwords",e).pack(pady=10)
j(R,"Toggle Theme",i).pack(pady=10)
x();R.mainloop()
