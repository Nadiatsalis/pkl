from django.shortcuts import render, redirect
from .forms import SpjForm, TanggalMerahForm
from .models import Spj, Uraian, TanggalMerah
from datetime import timedelta, date, datetime
from django.shortcuts import get_object_or_404

import datetime 
# from django.contrib.auth import logout_view

# Create your views here.

def index(request):
    title = 'List SPJ'
    spj = Spj.objects.all().order_by('-tgl_pembuatan')
    context = {
        'title':title,
        'spjs':spj
    }
    return render(request, 'app/index.html', context)

def home(request):
    spj = Spj.objects.all().order_by('-tgl_pembuatan')
    context = {
        'title':'Home',
        'spjs':spj
    }
    return render(request, 'app/home.html', context)


def tanggal_merah_create(request):
    if request.method == 'POST':
        form = TanggalMerahForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = TanggalMerahForm()
    else:
        form = TanggalMerahForm()
    context = {
        'title':'Tambah Tanggal Merah',
        'form':form
    }
    return render(request, 'app/tanggal_merah_create.html', context)

# def check_tanggal(request):
#     dt = datetime.datetime.now()
#     dt_month = dt.month
#     print(dt_month)
#     t_merah = TanggalMerah.objects.filter(tanggal_merah__month = dt_month)
#     tanggal_list = [i.tanggal_merah.day for i in t_merah]
#     # print(month_list)

#     spj = Spj.objects.get(pk=24)
#     spj_date = spj.tgl_pembuatan.day

#     if spj_date in tanggal_list:
#         print(True)
#         Spj.objects.create(tgl_pembuatan= date.today() + timedelta(days=4))
#     else:
#         print(False)

#     return render(request, 'app/check.html')


   

def create_spj(request):
    title = 'Tambah SPJ'
    dt = datetime.datetime.now()
    dt_month = dt.month
    # print(dt_month)
    t_merah = TanggalMerah.objects.filter(tanggal_merah__month = dt_month)
    tanggal_merah_list = [i.tanggal_merah.day for i in t_merah]
    # print(month_list)
    if request.method == 'POST':
        form = SpjForm(request.POST)
        if form.is_valid():
            spj = form.save()
            print(spj.tgl_pembuatan.strftime("%A"))
            tgl_pemb = date.today() + timedelta(days=1)
            tgl_pemb2 = date.today() + timedelta(days=2)
            # print(tgl_pemb not in tanggal_merah_list)

            if (tgl_pemb.strftime("%A") == 'Saturday') or (tgl_pemb.strftime("%A") =='Sunday'):
                if tgl_pemb not in tanggal_merah_list:
                    Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberitahuan PPTK', tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='PPTK/35.09.323')
                else:
                    Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberitahuan PPTK', tgl_pembuatan=date.today() + timedelta(days=2), no_surat='027', kode_surat='PPTK/35.09.323')
            
            else:
                if date.today() + timedelta(days=1) not in tanggal_merah_list:
                    Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberitahuan PPTK', tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='PPTK/35.09.323')
                else:
                    Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberitahuan PPTK', tgl_pembuatan=date.today() + timedelta(days=2), no_surat='027', kode_surat='PPTK/35.09.323')
                    
            #     if date.today() + timedelta(days=2) not in tanggal_merah_list:
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pengadaan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='PPK/35.09.323')
                    
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Undangan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='005', kode_surat='35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Penjelasan Pekerjaan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='BAPP/PBJ/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Penawaran Harga',  tgl_pembuatan=date.today() + timedelta(days=1),)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Pembukaan Penawaran, Evaluasi Klarifikasi dan Negosiasi',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='BAPEK/PBJ/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Berita Acara HPL',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='BAHPL/PBJ/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Penetapan Penyedia Barang/Jasa',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='SPPBJ/PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Kesanggupan Kerja',  tgl_pembuatan=date.today() + timedelta(days=1),)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat perintah Kerja (SPK)', tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='SPK/PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat Pesanan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='SP/PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat Pemberitahuan Pengiriman',  tgl_pembuatan=date.today() + timedelta(days=1),)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Undangan PPHP',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='005', kode_surat='35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Penerimaan Hasil Pekerjaan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='BAPHP', kode_surat='PPHP/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pencairan',  tgl_pembuatan=date.today() + timedelta(days=1))
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Pembayaran',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='BAP', kode_surat='35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Ringkasan Kontrak',  tgl_pembuatan=date.today() + timedelta(days=1)) 
            #     else:
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberitahuan PPTK', tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='PPTK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pengadaan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Undangan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='005', kode_surat='35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Penjelasan Pekerjaan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='BAPP/PBJ/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Penawaran Harga',  tgl_pembuatan=date.today() + timedelta(days=1),)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Pembukaan Penawaran, Evaluasi Klarifikasi dan Negosiasi',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='BAPEK/PBJ/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Berita Acara HPL',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='BAHPL/PBJ/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Penetapan Penyedia Barang/Jasa',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='SPPBJ/PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Kesanggupan Kerja',  tgl_pembuatan=date.today() + timedelta(days=1),)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat perintah Kerja (SPK)', tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='SPK/PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat Pesanan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='027', kode_surat='SP/PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat Pemberitahuan Pengiriman',  tgl_pembuatan=date.today() + timedelta(days=1),)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Undangan PPHP',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='005', kode_surat='35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Penerimaan Hasil Pekerjaan',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='BAPHP', kode_surat='PPHP/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pencairan',  tgl_pembuatan=date.today() + timedelta(days=1))
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Pembayaran',  tgl_pembuatan=date.today() + timedelta(days=1), no_surat='BAP', kode_surat='35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Ringkasan Kontrak',  tgl_pembuatan=date.today() + timedelta(days=1)) 
                
            #     if spj_date in tanggal_list:
            #         print(True)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberitahuan PPTK', tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='PPTK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pengadaan',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Undangan',  tgl_pembuatan=tgl_pemb2, no_surat='005', kode_surat='35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Penjelasan Pekerjaan',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='BAPP/PBJ/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Penawaran Harga',  tgl_pembuatan=tgl_pemb2)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Pembukaan Penawaran, Evaluasi Klarifikasi dan Negosiasi',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='BAPEK/PBJ/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Berita Acara HPL',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='BAHPL/PBJ/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Penetapan Penyedia Barang/Jasa',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='SPPBJ/PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Kesanggupan Kerja',  tgl_pembuatan=tgl_pemb2)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat perintah Kerja (SPK)', tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='SPK/PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat Pesanan',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='SP/PPK/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat Pemberitahuan Pengiriman',  tgl_pembuatan=tgl_pemb2)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Undangan PPHP',  tgl_pembuatan=tgl_pemb2, no_surat='005', kode_surat='35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Penerimaan Hasil Pekerjaan',  tgl_pembuatan=tgl_pemb2, no_surat='BAPHP', kode_surat='PPHP/35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pencairan',  tgl_pembuatan=tgl_pemb2)
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Pembayaran',  tgl_pembuatan=tgl_pemb2, no_surat='BAP', kode_surat='35.09.323')
            #         Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Ringkasan Kontrak',  tgl_pembuatan=tgl_pemb2)
            # #     Uraian.objects.create(tgl_pembuatan= date.today() + timedelta(days=4))

            # else:
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberitahuan PPTK', tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='PPTK/35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pengadaan',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='PPK/35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Undangan',  tgl_pembuatan=tgl_pemb2, no_surat='005', kode_surat='35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Penjelasan Pekerjaan',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='BAPP/PBJ/35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Penawaran Harga',  tgl_pembuatan=tgl_pemb2)
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Pembukaan Penawaran, Evaluasi Klarifikasi dan Negosiasi',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='BAPEK/PBJ/35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Berita Acara HPL',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='BAHPL/PBJ/35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Penetapan Penyedia Barang/Jasa',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='SPPBJ/PPK/35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Kesanggupan Kerja',  tgl_pembuatan=tgl_pemb2)
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat perintah Kerja (SPK)', tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='SPK/PPK/35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat Pesanan',  tgl_pembuatan=tgl_pemb2, no_surat='027', kode_surat='SP/PPK/35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Surat Pemberitahuan Pengiriman',  tgl_pembuatan=tgl_pemb2)
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Undangan PPHP',  tgl_pembuatan=tgl_pemb2, no_surat='005', kode_surat='35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Penerimaan Hasil Pekerjaan',  tgl_pembuatan=tgl_pemb2, no_surat='BAPHP', kode_surat='PPHP/35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pencairan',  tgl_pembuatan=tgl_pemb2)
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='BA Pembayaran',  tgl_pembuatan=tgl_pemb2, no_surat='BAP', kode_surat='35.09.323')
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Ringkasan Kontrak',  tgl_pembuatan=tgl_pemb2)
            return redirect('home')
            # else:
            #     pass
    else:
        form = SpjForm()
    context = {
            'title' : title,
            'form' : form
    }
    return render(request, 'app/form_spj.html', context)

def edit_spj(request,pk):
    spj = Spj.objects.get(id=pk)
    form = SpjForm(instance=spj)

    if request.method == 'POST':
        form = SpjForm(request.POST, instance=spj)
        if form.is_valid():
            form.save()
            return redirect('/home')

    context = {
        'title' : 'Edit SPJ',
        'form' : form
    }
    return render(request, 'app/form_spj.html', context)

def delete_spj(request, pk):
    spj = Spj.objects.get(id=pk)
    if request.method == "POST":
        spj.delete()
        return redirect('/home')

    context = {'item':spj}
    return render(request, 'app/delete.html', context)


def uraian(request, pk):
    # obj = get_object_or_404(Uraian, pk=pk)
    objs = Uraian.objects.filter(spj_id=pk)
    # title = '{} - {}'.format(obj.nama_uraian, obj.id)
    context = {
        'objs':objs,
        'title':'Uraian'
    }
    return render(request, 'app/uraian.html', context)


def tanggal_merah_create(request):
    if request.method == 'POST':
        form = TanggalMerahForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = TanggalMerahForm()
    else:
        form = TanggalMerahForm()
    context = {
        'title':'Tambah Tanggal Merah',
        'form':form
    }
    return render(request, 'app/tanggal_merah_create.html', context)

# def check_tanggal(request):
#     dt = datetime.datetime.now()
#     dt_month = dt.month
#     print(dt_month)
#     t_merah = TanggalMerah.objects.filter(tanggal_merah__month = dt_month)
#     tanggal_list = [i.tanggal_merah.day for i in t_merah]
#     # print(month_list)

#     spj = Spj.objects.get(pk=24)
#     spj_date = spj.tgl_pembuatan.day

#     if spj_date in tanggal_list:
#         print(True)
#         Spj.objects.create(tgl_pembuatan= date.today() + timedelta(days=4))
#     else:
#         print(False)

#     return render(request, 'app/check.html')


# def logout_view(request):
#     logout(request)

#     return render(request, 'spj/templates/login.html', context)





