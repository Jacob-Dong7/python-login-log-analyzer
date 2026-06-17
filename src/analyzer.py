class Analyzer:
    def __init__(self, file):
        self.file = file
        return
    
    def analyze(self):
        suspect_ip = {}
        for line in self.file:
            parts = line.split()
            
            if parts[3] == "status=failed":
                if parts[2] not in suspect_ip:
                    suspect_ip[parts[2]] = 1
                else:
                    suspect_ip[parts[2]] += 1
        risk_factor = self.sort(list(suspect_ip.items()))
        print(risk_factor)
            
        
    def sort(self, suspect):
        n = len(suspect)
        if n > 1:
            b = self.sort(suspect[0: n // 2 - 1])
            c = self.sort(suspect[n + 1: n - 1])
            return self.merge(b, c, suspect)
    
    def merge(self, b, c, a):
        i = 0
        j = 0
        k = 0
        while i < len(b) and j < len(c):
            if b[i][1] > c[j][1]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = c[j]
                j += 1
            k += 1

        while j < len(c):
            a[k] = c[j]
            j += 1
            k += 1
        while i < len(b):
            a[k] = b[i]
            i += 1
            k += 1
        return



        
                

        return