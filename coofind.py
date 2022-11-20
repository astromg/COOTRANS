#!/usr/bin/env python3



       elif ".raw" in self.coo_file or ".tfr" in self.coo_file or ".out" in self.coo_file or ".coo" in self.coo_file or ".als" in self.coo_file or ".lst" in self.coo_file or ".rsl" in self.coo_file: 
          for line in plik:
             if i>2 and len(line.split())>1: 
                self.ext_x.append(float(line.split()[1])-1.)
                self.ext_y.append(float(line.split()[2])-1.)
                self.ext_l.append(line)
             i=i+1
