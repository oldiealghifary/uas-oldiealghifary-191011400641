def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

class B_penanganan():
    s_lambat = 5
    lambat = 5
    cepat = 10

    def s_lambat(self, x):
        if x >= self.sedikit:
            return 0
        elif x<= self.s_lambat:
            return 1
        else:
            return down(x, self.s_lambat, self.lambat)

    def lambat(self, x):
        if x >= self.cepat:
            return 0
        elif x<= self.lambat:
            return 1
        else:
            return down(x, self.lambat, self.cepat)

    def cepat(self, x):
        if x >= self.cepat:
            return 1
        elif x<= self.lambat:
            return 0
        else:
            return up(x, self.lambat, self.cepat)

class K_pasien():
    sedikit = 10
    normal = 20
    ramai = 30
    s_ramai= 30


    
    def sedikit(self, x):
        if x >= self.normal:
            return 0
        elif x<= self.sedikit:
            return 1
        else:
            return down(x, self.normall,self.sedikit)

    def normal(self, x):
        if x >= self.ramai:
            return 0
        elif x<= self.normal:
            return 1
        else:
            return down(x, self.normal, self.ramai)

    def ramai(self, x):
        if x >= self.s_ramai:
            return 0
        elif x<= self.ramai:
            return 1
        else:
            return up(x, self.ramai, self.s_ramai)

    def s_ramai(self, x):
        if x >= self.s_ramai:
            return 1
        elif x<= self.ramai:
            return 0
        else:
            return up(x, self.ramai, self.s_ramai)

class fasilitas ():
    murah = 150.000
    standar = 250.000
    mahal = 500.000
    vip = 750.000

    def _lambat(self, a):
        return self.cepat - a*(self.cepat - self.lambat)

    def _cepat(self, a):
        return a*(self.cepat - self.lambat) + self.lambat

    def _inferensi(self, byk=B_Pasien(), ktr=K_pasien()):
        result = []
        
        a1 = min(byk.s_sedikit (self.ramai), ktr.rendah (self.))
        z1 = self._cepat(a1)
        result.append((a1, z1))
        
        a2 = min(byk.s_sedikit (self.ramai), ktr.normal (self.pasien))
        z2 = self._cepat(a1)
        result.append((a2, z2))
        
        a3 = min(byk.s_sedikit (self.ramai), ktr.vip (self.pasien))
        z3 = self.cepat(a3)
        result.append((a3, z3))

        a4 = min(byk.s_sedikit (self.ramai), ktr.tinggi (self.pasien))
        z4 = self._cepat(a4)
        result.append((a4, z4))
        
        a5 = min(byk.sedikit (self.ramai), ktr.rendah (self.pasien))
        z5 = self._cepat(a4)
        result.append((a5, z5))

        a6 = min(byk.sedikit (self.ramai), ktr.sedang (self.pasien))
        z6 = self._lambat(a6)
        result.append((a6, z6))

        a7 = min(byk.sedikit (self.ramai), ktr.tinggi (self.pasien))
        z7= self._cepat(a7)
        result.append((a7, z7))

        a8 = min(byk.sedikit (self.ramai), ktr.s_tinggi (self.pasien))
        z8 = self._lambat(a8)
        result.append((a8,z8))

        a9 = min(byk.ramai (self.ramai), ktr.rendah (self.pasien))
        z9 = self._lambat(a8)
        result.append ((a9,z9))

        a10 = min(byk.ramai (self.ramai), ktr.sedang (self.pasien))
        z10 = self._cepat (a10)
        result.append((a10,z10))

        a11 = min(byk.ramai (self.ramai), ktr.tinggi (self.kotor))
        z11 = self._cepat(a11)
        result.append((a11,z11))
        
        a12 = min(byk.ramai (self.ramai), ktr.s_tinggi (self.pasien))
        z12 = self._cepat(a12)
        result.append((a12,z12))
        return result
    
    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a