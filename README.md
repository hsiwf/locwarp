# LocWarp

**在 Windows 上控制 iPhone / iPad GPS 定位的虚拟定位工具。** 免越狱,通过 USB 或 WiFi 连接,支持瞬移、导航、多点路径、花农绕圈、随机漫步与摇杆操作,最多可同时控制三台设备。

<p align="right">
  <a href="README.md"><img alt="简体中文" src="https://img.shields.io/badge/简体中文-active-2d3748?style=flat-square"></a>
  <a href="README.en.md"><img alt="English" src="https://img.shields.io/badge/English-gray?style=flat-square"></a>
</p>

<p align="center">
  <img src="frontend/build/icon.png" width="128" alt="LocWarp">
</p>

<p align="center">
  <a href="https://github.com/keezxc1223/locwarp/releases">
    <img alt="下载安装包" src="https://img.shields.io/badge/下载安装包-4285f4?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <a href="#安装与前置设置">
    <img alt="安装说明" src="https://img.shields.io/badge/安装说明-2d3748?style=for-the-badge&logo=readthedocs&logoColor=white">
  </a>
  <a href="https://lin.ee/UwdCrmf" target="_blank">
    <img alt="LINE" src="https://img.shields.io/badge/LINE-联系作者-06C755?style=for-the-badge&logo=line&logoColor=white">
  </a>
</p>

<p align="center">
  <img src="docs/demo-v2.gif" width="720" alt="LocWarp demo">
</p>

## 目录

- [快速开始](#快速开始)
- [系统需求与兼容性](#系统需求与兼容性)
- [功能](#功能)
- [安装与前置设置](#安装与前置设置)
- [疑难解答](#疑难解答)
- [开发者文件](#开发者文件)
- [支持与联系](#支持与联系)
- [项目性质声明](#项目性质声明)
- [License](#license)
- [Disclaimer(免责声明)](#disclaimer免责声明)

---

## 快速开始

1. 到 [Releases](https://github.com/keezxc1223/locwarp/releases) 下载最新的 `LocWarp Setup x.y.z.exe` 并安装。
2. 电脑安装 iTunes 或 Apple Devices(提供 Apple USB driver)。
3. 用 USB 线接上 iPhone,在 iPhone 上点「信任这部电脑」。
4. iPhone 打开「设置 → 隐私权与安全性 → 开发者模式」。找不到这个选项时,LocWarp 连接后到「设置」页按「打开开发者模式」就会出现。
5. 打开 LocWarp(会要求系统管理员权限),在地图上按右键即可瞬移。

每个步骤的细节见[安装与前置设置](#安装与前置设置)。防毒软件若把后端程序误判隔离,请先把安装文件夹加入排除列表再重新安装。

---

## 系统需求与兼容性

| 项目 | 需求 |
| --- | --- |
| 电脑 | Windows 10 / 11(64 位元) |
| 设备 | iPhone / iPad,**iOS / iPadOS 17 以上**为主要支持版本 |
| iOS 16.x | 由社群维护(@bitifyChen,[#9](https://github.com/keezxc1223/locwarp/pull/9)),走 LegacyLocationService 路径 |
| iOS 15 以下 | 不支持 |
| 连接 | USB 线,或同一个 WiFi 网段(WiFi Tunnel 仅 iOS 17+) |

### 已回报可用的版本

| 主版本 | 已验证版本 |
| --- | --- |
| **iOS 27.x** | 27.0(开发者实测,iPhone 18 Pro Max) |
| **iOS 26.x** | 26.5 · 26.4.2 · 26.4.1 · 26.4.1 iPadOS · 26.4 · 26.3.1 · 26.2 · 26.2.1 iPadOS (M1 iPad) |
| **iOS 18.x** | 18.7.8 · 18.7.7 · 18.7.1 · 18.6.2 · 18.5 iPadOS · 18.3.1 · 18.1.1 |
| **iOS 17.x** | 17.6.1 |
| **iOS 16.x**(社群维护) | 16.7.15 · 16.7.12 |

「回报可用」代表**至少一位用户在其环境下成功运作**,不等同于通用兼容性保证。虚拟定位的稳定性取决于 iOS 修补版本、pymobiledevice3 对该版本的支持、Developer Disk Image 是否已挂载,以及 Windows 端的驱动、VPN、防火墙与防毒设置。没列在表上的 iOS 16+ 版本只是还没有人回报,欢迎到 [Issues](https://github.com/keezxc1223/locwarp/issues) 补充。

---

## 功能

### 移动模式

| 模式 | 说明 |
| --- | --- |
| **瞬移** | 直接跳到指定坐标 |
| **导航** | 从当前位置沿实际道路以走路、自行车或开车的速度前往目的地 |
| **多点路径** | 依序经过多个路径点,每站可停留(默认随机 5 到 20 秒)。圈数设 0 为跑一趟,设 N 为绕 N 圈,留空为无限循环 |
| **花农专用** | 在每个路径点周围绕圈。绕圈距离、每圈段数(3 到 20)、每点圈数(0.5 为半圈)、总轮数、每点前后等待都可以自订并保存,点与点之间可走过去或瞬移。面板会即时显示整趟预估时间,断线会自动重连续跑 |
| **随机漫步** | 在指定半径内随机漫游,每段停顿时间可调 |
| **摇杆** | 以方向和力度即时操控,支持 WASD 与方向键 |

多点路径可以勾选「**点对点跳跃**」,改成逐点瞬移而不走道路,适合只需要 GPS 依序停在每个点上的情况。跳跃前延迟(默认 2 秒)与跳跃后延迟(默认 4 秒)都可以调整,暂停时两段延迟都会冻结。

### 速度控制

- 三档默认:走路 10.8、自行车 19.8、开车 60 km/h。
- 可输入任意固定速度,或输入最小到最大的随机范围(例如 40 到 80 km/h),每段路重新抽一次,模拟真实路况。
- 移动进行中可以修改速度后按「套用新速度」,会从当前位置以新速度接续,不用停下重来。
- 选过的速度会记住,下次打开沿用。到点暂停时地图上方会显示倒数。

### 路径来源

导航与多点路径使用的道路路线,可以在四个免费、免注册的路径引擎之间切换:

| 引擎 | 说明 |
| --- | --- |
| **OSRM 公用 demo**(默认) | 全球涵盖,偶尔整个服务会中断 |
| **OSRM FOSSGIS** | 同样是 OSRM 引擎,由 FOSSGIS 代管的镜像 |
| **Valhalla** | 完全不同的引擎,两个 OSRM 节点都中断时最有用 |
| **BRouter** | 独立营运的第四个引擎,单车、健行、开车 profile 齐全 |

任何引擎失败时,该段路自动改走直线,下一段再重试,不会卡住。也可以直接勾选「使用直线路径」完全不查询引擎。多点路径另有「最佳顺序」功能,一键算出最短的走访顺序。

### 连接方式

- **USB**:插上自动连接,iPhone 锁定屏幕不受影响。拔除约 4 秒内检测到,重新插上自动恢复,不用刷新。
- **WiFi Tunnel**(iOS 17+,需先用 USB 配对过一次):
  - 「自动检测」会先用 mDNS 寻找设备,找不到再扫描局域网。
  - 连过的 IP 会记住,也可以「钉选」设备,之后每次启动自动连上,断线自动重试。
  - 「屏幕暗掉维持连接」(实验功能)会持续补送位置,降低 iPhone 锁定屏幕后断线的机率。
  - 「重新配对」可在配对记录损毁时,通过 USB 一键重建。
  - 停止 Tunnel 时若 USB 还插著,会自动切回 USB。

### 多设备群组模式

可同时连接**最多三台**设备。瞬移、导航、各种移动模式、暂停、继续、停止、套用速度、还原,都会同步送到所有设备,桌面与手机网页操控都适用。

- 启动任何动作前,会先把所有设备瞬移到同一个坐标,确保路径一致。
- 随机漫步使用相同的乱数种子,所有设备走的路线完全相同。
- 后来才接上的设备,会自动同步到当前位置并接续正在执行的任务。
- 每台设备可以个别还原、中断或打开开发者模式选项。

### 地图

- **图层切换**(右上角):OSM、Google 瓦片(测试)、ESRI 街道、ESRI 卫星、OpenFreeMap Liberty / Bright / Positron(向量图)、VersaTiles Colorful、NLSC 台湾电子地图、GSI 日本地理院地图。全部免 API key。
- 路径点以 S / 1 / 2 / 3 标示,路径线有流动箭头可以看出方向。
- 左上角按钮可一键置中当前的模拟位置。选「只显示路径」时地图会自动缩放到整条路线。
- 地图上的用户图示可以换成内建的 6 组角色,或上传自己的 PNG(自动去除透明边界)。
- 坐标格式可在 DD、DMS、DM 之间切换。

### 坐标收藏

- 新增坐标时自动带入地名与国旗,编辑后坐标改变会自动更新国旗。
- 分类可自订颜色,支持搜索、排序(名称 / 日期 / 最后使用)、拖动排序、多选删除。
- 导入与导出:JSON(全部资料,导入为合并不覆盖)、GPX(单笔、整个分类,或多个分类一次导出成 ZIP)。
- 可把所有收藏显示在地图上,数万笔也不会卡顿,密集的点会自动聚合。
- 「点击也要飞 GPS」可以决定点坐标时是真的瞬移过去,还是只把地图画面移过去看看。

### 保存路线

- 路线可以分类、拖动排序,并从列表直接加载开始跑。
- 支持 GPX 与 JSON 的导入导出。
- 可以把路径点依当前顺序复制成一行一笔的 `lat, lng` 文字。

### 地址搜索

- **免费版**:默认来源,使用 OpenStreetMap 开放资料,不用 API key。设置里另有 Photon 选项,模糊搜索与错字容错较强。
- **Google Geocoding**:输入自己的 API key(只存在本机),中文地名与店家结果最精准,每月有免费额度。
- 坐标输入框可以直接贴上坐标文字,会自动辨识出有效的经纬度。
- 手机网页操控会沿用电脑端的设置。

### 手机网页操控

人不在电脑旁时,可以用手机浏览器操控。按状态列的「手机操控」会显示局域网网址与 6 位数 PIN,手机输入后就能使用行动版地图:瞬移、导航到指定点(走路 / 自行车 / 开车或自订速度)、搜索地址、输入坐标、停止与还原,并即时显示桌面上同一条路径。

> 手机必须跟电脑连在**同一个 WiFi**,电脑防火墙需放行 8777 port。按「重新产生」可立刻更换 PIN,让之前配对过的手机失效。

### 状态列信息

- 当前模拟位置的**国旗、地名、当地天气与温度**。
- 跨时区时显示时差,点开可看完整时区信息。
- **一键还原**:清除虚拟定位。注意「停止」只会结束移动,虚拟定位仍然保留,要恢复真实 GPS 请按还原。
- 版本号:有新版本时旁边出现 `NEW` 标示,点击前往下载页。
- 「Log 文件夹」按钮:一键打开 `~/.locwarp/logs/`,方便把 backend.log 附到 Issue。

### 其他

- **Cooldown**:依瞬移距离自动计算冷却时间,降低被检测为异常移动的风险。
- 界面语言可在简体中文与 English 之间即时切换。
- 路线完成提示音、硬件加速开关(部分显示卡驱动下关闭可解决残影或黑画面,见 [Issue #24](https://github.com/keezxc1223/locwarp/issues/24))。
- 所有资料(坐标收藏、路线、设置)都存在 `~/.locwarp/`,重新安装不会遗失。

---

## 安装与前置设置

**[下载安装包](https://github.com/keezxc1223/locwarp/releases)**。安装包已包含所有需要的组件,不用另外安装 Python 或 Node。安装后从桌面或开始菜单打开 **LocWarp**,启动时会要求系统管理员权限(WiFi Tunnel 建立虚拟网络接口需要)。

### 1. 安装 Apple USB driver

Windows 需要 Apple 的 USB driver 才能跟 iPhone 沟通。下列**择一**安装即可:

- [iTunes for Windows(桌面版,64-bit)](https://secure-appldnld.apple.com/itunes12/047-76416-20260302-fefe4356-211d-4da1-8bc4-058eb36ea803/iTunes64Setup.exe)
- [Microsoft Store 的 iTunes](https://apps.microsoft.com/detail/9pb2mz1zmb1s)
- [Microsoft Store 的 Apple Devices](https://apps.microsoft.com/detail/9np83lwlpz9k?hl=zh-TW&gl=TW)

多数人装桌面版 iTunes 就能用。如果 iTunes 抓不到 iPhone,社群回报改装 Apple Devices 可以成功。

### 2. USB 连接并信任此电脑

第一次使用前用 USB 线接上 iPhone,iPhone 会询问「要信任这部电脑吗?」,点**信任**并输入密码。

### 3. 打开开发者模式

iPhone 上:**设置 → 隐私权与安全性 → 开发者模式 → 打开**,设备会要求重新启动,重启后再确认一次。

iOS 16 以上默认不显示这个选项。LocWarp 连上设备后,到上方的「**设置**」页按「**打开开发者模式**」按钮,按下后:

1. 在 iPhone 上完全关掉「设置」App。
2. 重新打开「设置 → 隐私权与安全性」,往下拉就会看到「开发者模式」。
3. 打开它,依指示重新启动。

按钮不能用的时候(例如只有 WiFi 连接),可以改用[侧载 IPA 的备援方式](#附录用侧载方式让开发者模式出现)。

### 4. 挂载 Developer Disk Image(iOS 17+)

iOS 17 以上需要 iPhone 上挂有 Personalized DDI 才能模拟定位。LocWarp 只会检查,不会自动下载或挂载。如果提示「iPhone 上未检测到 DDI」,请用下列任一工具帮 iPhone 挂一次:Xcode、爱思助手、3uTools、pymobiledevice3 CLI。

### 5. WiFi Tunnel(选用)

想拔掉 USB 改用无线时:

- iPhone 与电脑必须在**同一个 WiFi 网段**。
- 必须先完成步骤 2 的 USB 配对。
- 在 LocWarp 的「连接」页启动 WiFi Tunnel,成功后即可拔除 USB。

| 连接方式 | iPhone 锁定屏幕 | 建议 |
| --- | --- | --- |
| **USB** | 不受影响 | 无 |
| **WiFi Tunnel** | 会让网络接口休眠,连接中断 | 关闭自动锁定,或打开「屏幕暗掉维持连接」 |

使用 WiFi Tunnel 时建议把「设置 → 显示与亮度 → 自动锁定」设为**永不**,并接上充电线。

---

## 疑难解答

| 症状 | 可能原因与解法 |
| --- | --- |
| 打开后显示后端程序不存在 | 防毒软件把未签名的后端 exe 隔离了。把安装文件夹加入排除列表后重新安装 |
| Tunnel 启动后连不上 | 确认以系统管理员身份启动;暂时关闭 VPN 或第三方防火墙再试 |
| WiFi 自动检测找不到设备 | 确认在同一个 WiFi 网段、路由器没有打开设备隔离(AP isolation);可改为手动输入 IP |
| `No such service: com.apple.instruments.dtservicehub`,或提示「未检测到 DDI」 | 依[步骤 4](#4-挂载-developer-disk-imageios-17)挂载 DDI。仍失败时,先把开发者模式关闭、重开机、再次打开,然后重新挂载 |
| iPhone 设置里找不到开发者模式 | LocWarp 连上设备后,到上方的「设置」页按「打开开发者模式」,再依[步骤 3](#3-打开开发者模式)关掉并重开 iPhone 的「设置」App。按钮无效时改用[侧载方式](#附录用侧载方式让开发者模式出现) |
| 画面残影或黑画面 | 在「设置」页关闭硬件加速 |
| 打开程序直接闪退 | 新版会自动改为软件渲染并重启;仍闪退的话,对捷径按右键 › 内容 › 目标,结尾补上 `--no-sandbox --disable-gpu --in-process-gpu` |
| 国旗或地名没有出现 | 这两项来自免费的公共服务,偶尔会暂时无回应,稍后再瞬移一次即可 |

回报问题时请附上 iOS 版本、连接方式,以及 `~/.locwarp/logs/backend.log`。

### 附录:用侧载方式让开发者模式出现

1. 安装 [Sideloadly](https://sideloadly.io/)。
2. 从 [Decrypt IPA Store](https://decrypt.day/) 或 [ARM Converter Decrypted App Store](https://armconverter.com/decryptedappstore/us) 取得任意一个 IPA,建议挑体积小的。
3. 把 IPA 拖进 Sideloadly,USB 接上 iPhone,输入个人 Apple ID 后按 **Start**。
4. 完成后,iPhone 的「设置 → 隐私权与安全性」最下方会出现「开发者模式」,打开并重新启动。

---

## 开发者文件

### 架构

```
┌─────────────────┐      IPC / HTTP + WS       ┌──────────────────┐
│ Electron + React│ ─────────────────────────► │ FastAPI backend  │
│  (port 5173 dev)│ ◄───────────────────────── │  (port 8777)     │
└─────────────────┘                            └────────┬─────────┘
                                                        │ pymobiledevice3
                                                        ▼
                                              ┌──────────────────┐
                                              │ iPhone (USB/WiFi)│
                                              └──────────────────┘
```

### 技术组成

| 层 | 技术 | 用途 |
| --- | --- | --- |
| Frontend | [Electron](https://www.electronjs.org/) 44 | 桌面外壳,负责窗口、启动 backend、改写瓦片请求的 User-Agent |
| Frontend | [React](https://react.dev/) 19 + [TypeScript](https://www.typescriptlang.org/) 7 + [Vite](https://vitejs.dev/) 8 | UI 与打包(`base: './'` 供 `file://` 加载) |
| Frontend | [Leaflet](https://leafletjs.com/) 1.9 | 互动地图、自订标记、动画路径线 |
| Frontend | [MapLibre GL](https://maplibre.org/) 6 | 向量图层渲染,经 maplibre-gl-leaflet 挂进 Leaflet |
| Backend | Python 3.13 + [FastAPI](https://fastapi.tiangolo.com/) + [uvicorn](https://www.uvicorn.org/) | REST API 与 WebSocket(`:8777`) |
| Backend | [pymobiledevice3](https://github.com/doronz88/pymobiledevice3) 11.49+ | iOS 设备协议(DVT / RemoteServices / lockdown / LegacyLocationService)与 WiFi tunnel |
| Backend | [httpx](https://www.python-httpx.org/)、[pydantic](https://docs.pydantic.dev/)、[gpxpy](https://github.com/tkrajina/gpxpy) | 外部服务呼叫、资料验证、GPX 解析 |
| 打包 | [PyInstaller](https://pyinstaller.org/)、[electron-builder](https://www.electron.build/)(NSIS) | backend exe 与 Windows 安装包 |

界面图示全部是 inline SVG,样式是手写的单一 `styles.css`,没有使用第三方 icon 或 UI 组件库。

### 外部服务

全部免费。除了 Google Geocoding 需要用户自备 key,其余都不需要注册。

| 服务 | 呼叫端 | 用途 |
| --- | --- | --- |
| [OSRM demo](https://project-osrm.org/)、[OSRM FOSSGIS](https://routing.openstreetmap.de/)、[Valhalla](https://valhalla1.openstreetmap.de/)、[BRouter](https://brouter.de/) | backend | 路线规划与多点顺序最佳化 |
| [Photon (komoot)](https://photon.komoot.io/) | backend | 地址搜索与反向地理编码(国旗、地名) |
| [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding) | backend | 地址搜索(选用,用户自备 key) |
| [Open-Meteo](https://open-meteo.com/) | frontend | 模拟位置的天气 |
| [TimezoneDB](https://timezonedb.com/) | backend | 坐标转时区(内建 key) |
| [flagcdn.com](https://flagcdn.com/) | frontend | 国旗图片 |
| OpenStreetMap、Google、[ESRI](https://www.esri.com/)、[OpenFreeMap](https://openfreemap.org/)、[VersaTiles](https://versatiles.org/)、[NLSC](https://maps.nlsc.gov.tw/)、[GSI](https://www.gsi.go.jp/) | frontend | 地图瓦片 |
| [GitHub Releases](https://github.com/keezxc1223/locwarp/releases) | frontend | 启动时检查新版本(无遥测) |

反向地理编码不使用 Nominatim 公共服务器,因为它的使用政策以应用程序为单位计算流量上限,不适合散布型的桌面程序。地址搜索的默认选项若被 Nominatim 拒绝,会自动改用 Photon。

### 核心模块(`backend/core/`)

| 模块 | 职责 |
| --- | --- |
| `simulation_engine.py` | 中央控制器:状态转换、任务生命周期、`_move_along_route()` 移动回圈、ETA 计算 |
| `device_manager.py` | 设备探索、USB 与 WiFi Tunnel 连接管理 |
| `navigator.py` | 单一目的地导航 |
| `route_loop.py` / `multi_stop.py` | 多点路径的循环与停留 |
| `flower.py` | 花农专用的绕圈逻辑 |
| `random_walk.py` / `joystick.py` | 随机漫步、摇杆 |
| `teleport.py` / `restore.py` | 瞬移、还原 |

### 设计重点

- **位置推播**:backend 每个 tick 通过 WebSocket 送出 `position_update`,前端即时更新地图与 ETA。
- **速度解析**:`config.resolve_speed_profile()` 统一处理模式默认、固定速度、随机范围,优先序为范围 > 固定 > 默认。
- **In-process WiFi tunnel**:backend 直接在主 event loop 内执行 `start_tcp_tunnel()`,没有独立的 helper 程序。
- **状态目录**:所有执行期资料写入 `~/.locwarp/`,避开 PyInstaller 的临时目录。
- **节制的地理查询**:国旗、地名、时区、天气只在静止或瞬移后、且位置变动超过 100 米时查询,移动中不查,避免干扰与设备的通讯。四项查询并行,其中一项慢不会拖住其他项。
- **反向地理编码缓存**:结果以约 100 米的格子为单位存在磁盘(`reverse_geocode_cache.json`,保留 30 天),回到查过的地方不再连网,同时发出的相同查询会合并成一次。新增坐标与「这里是哪里」会略过缓存以取得精确名称。
- **天气由前端直连**:每个用户用自己的 IP 计算 Open-Meteo 配额,不经 backend 转送。
- **图层预先连接**:滑鼠移到图层菜单时,预先对所有图层的主机建立连接并抓取向量图层的 style,缩短第一次切换的等待。
- **多设备群组**:primary 设备不会被后插的设备取代,后插的设备会同步到 primary 的位置并接续任务。

### 开发环境

需求:Windows 10 / 11、Python **3.13**、Node.js 18+,以及一台已配对并打开开发者模式的 iPhone。

```bash
# 后端依赖(含 WiFi tunnel)
py -3.13 -m pip install -r backend/requirements.txt

# 前端依赖
cd frontend
npm install
```

双击 `LocWarp.bat` 会自动提权并启动 backend(`:8777`)与 Vite dev server(`:5173`),并用默认浏览器打开。也可以手动启动:

```bash
# 终端 1:backend
cd backend && py -3.13 main.py

# 终端 2a:前端走浏览器
cd frontend && npx vite --host --port 5173

# 终端 2b:前端走 Electron 窗口(跟安装包相同的执行方式)
cd frontend && npm run start
```

> 开发模式走 `http://`,安装包走 `file://`,两者行为不完全相同(例如 MapLibre 的 worker)。升级前端依赖包后,请务必用打包后的安装包验证。

### 打包

```bash
# 一次性安装
py -3.13 -m pip install pyinstaller
cd frontend && npm install -D electron-builder

# 一键建置
build-installer.bat
```

`build-installer.bat` 依序执行:

1. **PyInstaller** 编译 backend 到 `dist-py/locwarp-backend/`
2. **Vite** 建置前端到 `frontend/dist/`
3. **electron-builder** 产出 `frontend/release/LocWarp Setup X.Y.Z.exe`(约 175 MB)

注意 `npm run dist` 只执行第 3 步。改过 backend 要重跑 PyInstaller,改过前端或版本号要重跑 `npx vite build`,否则安装包会带到旧的内容。

### 项目结构

```
locwarp/
├── backend/                 # FastAPI + pymobiledevice3
│   ├── api/                 # HTTP endpoints
│   ├── core/                # Simulation engine + 各移动模式
│   ├── services/            # 定位服务、地理编码、坐标收藏、路线
│   ├── models/schemas.py    # Pydantic models
│   ├── static/phone.html    # 手机网页操控页面
│   ├── config.py            # 速度 profile、cooldown 表、路径设置
│   ├── main.py              # Entrypoint
│   └── locwarp-backend.spec # PyInstaller spec
│
├── frontend/                # Electron + React
│   ├── electron/main.js     # Electron 进入点,打包模式下启动 backend
│   ├── src/
│   │   ├── App.tsx
│   │   ├── components/      # MapView, ControlPanel, BookmarkList, StatusBar...
│   │   ├── hooks/           # useSimulation, useDevice, useBookmarks
│   │   ├── i18n/            # 中英文字符串
│   │   └── services/api.ts
│   ├── build/               # 图示与安装程序图片
│   └── package.json         # electron-builder 设置
│
├── LocWarp.bat / start.py   # 开发用启动器(自动提权)
├── stop.py
└── build-installer.bat      # 一键建置安装包
```

---

## 支持与联系

有问题、建议,或想回报某个 iOS 版本可用,欢迎[加 LINE](https://lin.ee/UwdCrmf) 或到 [Issues](https://github.com/keezxc1223/locwarp/issues) 留言。

### USDT 斗内(TRC-20 / TRON 链)

LocWarp 免费且开源。想支持开发的话,可以使用下方地址。**仅支持 TRC-20(TRON 链)**,请勿使用其他链转帐。

```
TB1i7pEcifAeh8oDLLZFqiRVrpUaZmmDAn
```

<p>
  <img src="docs/donate-usdt-tron-qr.png" alt="USDT TRC-20 QR" width="260">
</p>

---

## 项目性质声明

LocWarp 是个人独立维护的开源项目,不是商业产品,也没有专职团队。开发者会尽力在合理时间内新增功能、回应 Issue、修复 Bug,并随 iOS 与 pymobiledevice3 的版本演进持续更新,但是:

- 本项目只保证在**开发者本人的测试环境**(当前为 iPhone 18 Pro Max / iOS 27.0 + Windows 11 专业版)下运作正常;
- **不保证在其他设备、iOS 修补版本、网络环境、系统配置下都能稳定使用**;
- 遇到问题时,欢迎到 [Issues](https://github.com/keezxc1223/locwarp/issues) 提交完整的环境信息与日志,协助定位与改善;
- 本项目不保证永续维护,也不承担因使用本工具所生的任何责任。

---

## License

本项目采用 **MIT License** 授权释出,详见 [LICENSE](LICENSE)。

允许自由使用、修改、再散布与商业利用,惟须保留原始著作权与授权声明。

---

## Disclaimer(免责声明)

### 1. 仅限学术与研究用途

本项目开发初衷仅供地理信息系统(GIS)研究、行动应用程序开发测试、位置服务原型验证及相关技术探讨使用。请勿将本工具用于任何非法用途,或违反第三方服务条款、平台政策之行为。

### 2. 帐号封禁风险

本项目通过 pymobiledevice3 介接 Apple DVT / RemoteServices 协议,以模拟 GPS 信号达成虚拟定位。若将本工具用于基于地理位置的游戏(例如 Pokémon GO、Ingress、Monster Hunter Now 等)或社交、打卡、物流类应用,可能违反该平台的服务条款,进而导致帐号遭警告、限制、封锁或永久停权。**开发者对因使用本工具所造成之任何帐号损失、虚拟财产损害或衍生纠纷,概不负责。**

### 3. 系统与硬件风险

本项目于 WiFi Tunnel 模式下需以**系统管理员权限**执行,以建立 TUN 虚拟网络接口并与 iOS 设备协商 RSD(Remote Service Discovery)通道。虽然代码已经内部测试,但开发者不保证于所有 Windows 版本、硬件组合、网络环境下皆能稳定运行。常见的潜在状况包括:

- 与 VPN 软件、第三方防火墙或网络虚拟化工具发生冲突,导致 Tunnel 建立失败或系统网络暂时异常
- 程序非正常结束时残留的 TUN 接口需重新启动系统始能清除
- 连接中断时需手动重试或重启应用程序

用户应自行评估上述风险并承担因此所产生之任何后果。本项目仅操作本身所建立之临时网络接口与自身配置文件(位于 `~/.locwarp/`),**不会修改 iOS 设备内任何用户资料,亦不会变更操作系统核心文件或既有设备配对记录**。

### 4. 地图资料准确性

本项目前端采用 Leaflet,底图由 OpenStreetMap 及其他第三方瓦片供应商提供,路线规划使用 OSRM、Valhalla 与 BRouter 公共服务,地理编码使用 Photon 等公共服务。地图显示之坐标、路径、地址信息**仅供参考**,开发者不保证其完整性、即时性、正确性或与实际地理位置完全一致。用户在依照地址搜索、路线导航、随机漫步等结果进行定位模拟前,应自行比对地图显示是否符合预期。

### 5. 用户责任

用户应自行遵守所在地之法律法规,包括但不限于《个人资料保护法》《著作权法》及相关国际条约。任何因滥用、误用或违法使用本工具所引发之法律纠纷、民事赔偿或刑事责任,均由用户个人独自承担,与本项目之开发者及贡献者无涉。

---

**下载、安装或执行本软件,即视为您已完整阅读并同意上述全部免责条款。**

**若不同意,请立即停止使用并移除本软件。**
