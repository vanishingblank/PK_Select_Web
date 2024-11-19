# PK_Select_Web
若将该项目在局域网中可访问，请事先ipconfig自己电脑在当前网络的ip,并填写到前端的axios，后端的cors

如果想省事请配置好vite.config.js的proxy(调试时使用)

tips:
查看当前局域网空闲ip:
```for /L %i in (1,1,254) do @ping -n 1 -w 1 192.168.1.%i | findstr /R /C:"TTL="```


Official:


