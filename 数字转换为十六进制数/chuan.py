class Solution(object):
    def toHex(self, num):
        zimu = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        if num >= 0:
            ret = ''
            zheng = bin(num)[2:]
            while zheng:
                bei = zheng[-4:]
                zheng = zheng[:-4]
                zz = int(bei, 2)
                if zz > 9:
                    zz = zimu.get(zz)
                ret = str(zz) + ret
        else:
            # 首先先将用正数处理
            num = abs(num)
            ret = ''
            bb = num ^ 0xffffffff
            zheng = bin(bb+1)[2:]
            while zheng:
                bei = zheng[-4:]
                zheng = zheng[:-4]
                zz = int(bei, 2)
                if zz > 9:
                    zz = zimu.get(zz)
                ret = str(zz) + ret
        return ret