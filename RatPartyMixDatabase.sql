-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: testxd
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `artists`
--

DROP TABLE IF EXISTS `artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artists` (
  `artist_id` int unsigned NOT NULL AUTO_INCREMENT,
  `spotify_id` varchar(255) NOT NULL,
  `artist_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`artist_id`),
  UNIQUE KEY `spotify_id` (`spotify_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1791 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
INSERT INTO `artists` VALUES (299,'4IwOItqRhsIoRuD5HP4vyC','Slint'),(300,'3JVF9a4IJrL7sTSdjXxIqJ','Eddie Hazel'),(301,'7M1FPw29m5FbicYzS2xdpi','King Crimson'),(302,'0epOFNiUfyON9EYx7Tpr6V','The Strokes'),(303,'3IWdvItNhmdo282Wwp0CwH','Tamino'),(304,'0TMvoNR0AIJV138mHY6jdE','sanah'),(305,'53l3yjX8ITilPIlCRsVKEB','Kwiat Jabłoni'),(307,'5bQZCiENsgmW4SvUOc86qI','Grzegorz Turnau'),(308,'2JN7EU0IQBx2cWaHh23Mfm','Grzegorz Hyży'),(309,'01XYiBYaoMJcNhPokrg0l0','STAYC'),(310,'762310PdDnwsDxAQxzQkfX','Depeche Mode'),(311,'7CJgLPEqiIRuneZSolpawQ','Taco Hemingway'),(312,'6deZN1bslXzeGvOLaLMOIF','Nickelback'),(313,'6Ghvu1VvMGScGpOUJBAHNH','Deftones'),(329,'77QIEno3j2L5WkrHkh2OnP','Sir Mich'),(330,'0Zp66HyrElu0P3dErQGrF3','Alijandro'),(331,'1rbcX4vPiB7U03QhnbkA8d','Kenny'),(332,'6RHTUrRF63xao58xh9FXYJ','IVE'),(352,'46SHBwWsqBkxI7EeeBEQG7','Kodak Black'),(353,'0ErzCpIMyLcjPiwT4elrtZ','NLE Choppa'),(354,'1oSPZhvZMIrWW5I41kPkkY','Jimin'),(355,'164Uj4eKjl6zTBKfJLFKKK','JVKE'),(356,'7tjVFCxJdwT4NdrTmjyjQ6','Muni Long'),(357,'1lpOgw56wZLDa8gaP6bSIs','Fast & Furious: The Fast Saga'),(411,'4gzpq5DPGxSnKTe4SA8HAU','Coldplay'),(412,'3Nrfpe0tUJi4K4DXYWgMUX','BTS'),(413,'0k17h0D3J5VfsdmQ1iZtE9','Pink Floyd'),(441,'1McMsnEElThX1knmY4oliG','Olivia Rodrigo'),(442,'1fZAAHNWdSM5gqbi9o5iEA','Chivas'),(578,'6CP5wWvO8oIxedESJNCN4H','Ski Aggu'),(579,'6s5ubAp65wXoTZefE01RNR','Joost'),(580,'1T6DQ853AlyL47W8a2jC0f','Otto Waalkes'),(641,'4tZwfgrHOc3mvqYlEYSvVi','Daft Punk'),(642,'2RdwBSPQiwcmiDo9kixcl8','Pharrell Williams'),(643,'3yDIp0kaq9EFKe07X1X2rz','Nile Rodgers'),(644,'47zz7sob9NUcODy0BTDvKx','Sade'),(737,'7hJcb9fa4alzcOq3EaNPoG','Snoop Dogg'),(738,'1Cs0zKBU1kc0i8ypK3B9ai','David Guetta'),(739,'39unIFnj3C60Q4FtYdS7fW','Giorgio Tuinfort'),(740,'6mr36E8GEO5zhtL71GCrZ5','Frederic Riesterer'),(742,'0z4gvV4rjIZ9wHck67ucSV','Akon'),(743,'7sfl4Xt5KmfyDs2T3SVSMK','Lil Jon'),(744,'3sgFRtyBnxXD5ESfmbK4dl','LMFAO'),(745,'3FsSVftcI1h7LpH1NYI5nS','Bracia Figo Fagot'),(746,'4NtiLs5NpjgZDHNBEMbjKz','Popek'),(747,'2oaS92UgwaW2apuyT42OdQ','Tańcula'),(748,'20akE7sZUTpZSC78lPhqvt','Cypis'),(749,'45hBjirhIA7hFbKc54S7kG','Zamyślak'),(750,'0jnsk9HBra6NMjO2oANoPY','Flo Rida'),(751,'0TnOYISbd1XYRBk9myaseg','Pitbull'),(753,'5wC49IjPj5E1H2fGasAnOm','Cypis & Kaczmi & Popek'),(755,'3aQeKQSyrW4qWr35idm0cy','T-Pain'),(756,'1HY2Jd0NmPuamShAr6KMms','Lady Gaga'),(759,'33ScadVnbm2X8kkUqOkC6Z','Don Omar'),(760,'5bv5RplEOwdCvhq0EILh9E','Lucenzo'),(761,'01CC0QaWv9hM4Eroe6ZKHw','Remady & Manu-L'),(762,'0aImibWL2VPitiLu5WyiOA','J-Son'),(763,'0eDvMgVFoNV3TpwtrVCoTj','Pop Smoke'),(764,'0Ol3Jol2T3lZZVLNNzWPhj','R.I.O.'),(765,'56JVNVix1HgLwxGGHnSAdq','Nicco'),(766,'16IE8lpWA2U3bfB4kumGzW','After Party'),(768,'6yTYR09WCvsgdnurDW4WQo','DJ Antoine'),(769,'3yBEHAINorE3uSvsCmyCwQ','Mad Mark'),(770,'4VrsQ3yEvy6XOfhwsbiWAE','B-Case'),(771,'0ufZ8aJddoH64opBEf6bMI','U-Jean'),(772,'5K4W6rqBFWDnAN6FQUkS6x','Kanye West'),(773,'0c173mlxpT3dSFRgMO8XPh','Big Sean'),(774,'0ONHkAv9pCAFxb0zJwDNTy','Pusha T'),(775,'17lzZA2AlOHwCwFALHttmp','2 Chainz'),(777,'3oLccEy7y6zTe1gCFHxuWr','Timati'),(778,'2NoFr6doacvN58q9p9EFky','Kalenna'),(779,'6MF9fzBmfXghAz953czmBC','Taio Cruz'),(780,'2DlGxzQSjYe5N6G9nkYghR','Jennifer Lopez'),(782,'30n2M66Hu0LvcaRAJDrcxQ','K Koke'),(783,'1Kjs5u8GQf6zCFdTj6SI9E','Malik Montana'),(784,'3ZASW3RrHBbSRkNLjOrAFF','Sasha Lopez'),(785,'3TaUSUXn41GixL7zbvrIDt','A-Trak'),(786,'18HVMQsV3tINaTyzT5UIjH','CyHi'),(787,'2D3CXS70FRMw2FIkchBQdH','Casper & B.'),(788,'1ruutHJcECI7cos2n5TqpO','Nayer'),(789,'31TPClRtHm23RisEBtV3X7','Justin Timberlake'),(790,'5Y5TRrQiqgUO4S36tzjIRZ','Timbaland'),(791,'413WU2eol6xPjgigGX5ee8','P.I.WO BOYZ GANG'),(792,'0x4xJCGDyTlKr47RF2WXzu','Trill Pem'),(793,'5AmZdY72O0NVE0XxWdMfxv','Wac Toja'),(794,'5pKCCKE2ajJHZ9KAiaK11H','Rihanna'),(795,'07YZf4WDAMNwqr4jfgOZ8y','Jason Derulo'),(800,'4Ws2otunReOa6BbwxxpCt6','Benny Benassi'),(801,'1jQDgp9Fak4WYVZedWLF4G','The Biz'),(803,'5FTpdDUA9cksspPW5Ix78g','U-Jean'),(805,'2L8yW8GIoirHEdeW4bWQXq','TJR'),(808,'698hF4vcwHwPy8ltmXermq','Far East Movement'),(809,'7C64wNX3howEFZjAYRKsfP','The Cataracs'),(810,'7Ip2u3e5Nv6fFb5xyIHxEE','DEV'),(811,'7A8S43ryYdbWpJKeHRZRcq','JACKBOYS'),(813,'0Y5tJX1MQlPlqiwlOH1tJY','Travis Scott'),(815,'5LHRHt1k9lMyONurDHEdrp','Tyga'),(816,'0hCNtLu0JehylgoiP8L4Gh','Nicki Minaj'),(817,'3Isy6kedDrgPYoTS1dazA9','Sean Paul'),(819,'1oxn6cQ37twQ7yGnlE3ETd','Oki'),(820,'1yq2JzsqbzFbJ1B7wGOXLc','Young Igi'),(821,'4zvO09rVUIVTeALhs6xLoB','Otsochodzi'),(822,'5VnJPtvfHh4fPlHDzXjvLP','OIO'),(825,'1KJvuZHmkpnrjIyTLhhwpb','Solar'),(826,'2ufQfSFDFXfMS7MEMzdGZE','Białas'),(827,'3gm9b6AeMf2eGQTLashkDt','Deemz'),(828,'52vstSwpIEImkm06cG6kJD','GOMBAO 33'),(829,'0iBTVnJ1Sff92zCDujfvyJ','Young Leosia'),(830,'0QR764k0D36npmTMWx5bft','Żabson'),(832,'7HhC70MoKQYjd2lnF5Znhs','Oliwka Brazil'),(833,'77AiFEVeAVj2ORpC85QVJs','Steve Aoki'),(834,'4RSyJzf7ef6Iu2rnLdabNq','Willy William'),(836,'2oQX8QiMXOyuqbcZEFsZfm','El Alfa'),(837,'23TFHmajVfBtlRx5MXqgoz','Sfera Ebbasta'),(838,'7MP4jhYmFEgb0AtiOkw55s','Play-N-Skillz'),(840,'085pc2PYOi8bGKj0PNjekA','will.i.am'),(841,'26dSoYclwsYLMAKD3tpOr4','Britney Spears'),(845,'50co4Is1HCEo8bhOyUWKpn','Young Thug'),(847,'6nStjcAtMWhraEtrTrePkl','DaChoyce'),(848,'0Kwf0zcciIFGLCKiqNcO6Q','SRNO'),(849,'5r3fI2q1YU3QyVP7oncOQ9','The Plug'),(850,'0AEQNlJAZeghMaFyIYfrQG','SB Maffija'),(852,'2LI7lXaNJU420lffFWJUcT','Pedro'),(853,'6HdxibJzoNkDUUDHagx3Ko','francis'),(855,'6LqNN22kT3074XbTVUrhzX','Kesha'),(857,'4rneSQYWhgIT9pMX2NwpeM','Ekipa'),(858,'1efYxTvCNTpqYqfiEsxawq','Jacuś'),(859,'23zg3TcAtWQy7J6upgbUnj','Usher'),(861,'3ipn9JLAPI5GUEo4y4jcoi','Ludacris'),(862,'1A6HQzOvtGaCYihOuIKjE6','Mr. Polska'),(863,'4Q3xLVaD2uBZGVxmCYuSkt','Kabe'),(864,'2IHoZ3RrDJIikMRsYgHjhy','Kizo'),(867,'3q7HBObVc0L8jNeTe5Gofh','50 Cent'),(868,'5YBSzuCs7WaFKNr7Bky0Uf','Olivia'),(869,'7pFeBzX627ff0VnN6bxPR4','Desiigner'),(870,'7gZfnEnfiaHzxARJ2LeXrf','6ix9ine'),(872,'4kYSro6naA4h99UJvo89HB','Cardi B'),(873,'181bsRPaVXVlUKXrxwZfHK','Megan Thee Stallion'),(875,'5YtG8ex3jLuNHgS6TqQAux','Magik Band'),(878,'51GeNlazymktHPTNn8aEyn','ZetHa'),(879,'2V5xArcB3BGAHmwsK46tyU','Vladimir Cauchemar'),(881,'56VhOZOF6hwqrbNYwkmcsH','Sobel'),(882,'58HrJf2URKRHTdaB28FcLh','PSR'),(884,'2tWk9y3smAR3vNuC2ovMaB','NATEGAWD'),(888,'4DdkRBBYG6Yk9Ka8tdJ9BW','Offset'),(890,'79b4a4Bg30Y0RlO5de5jni','Alberto'),(891,'4RoVw3AbSvjr1KFpzjBZgA','Josef Bratan'),(894,'21E3waRsmPlU7jZsS13rcj','Ne-Yo'),(895,'4D75GcNG95ebPtNvoNVXhz','AFROJACK'),(897,'37GUqxafAvAKGMZbXCUnmr','Mohombi'),(901,'4VMYDCV2IEDYJArk749S6m','Daddy Yankee'),(904,'3mH3OBKopDDVgnJcT5PrPk','Redfoo'),(905,'3qb0oGqshqtUmp7AMfKoZi','DR. VODKA'),(907,'6PcYcDQ7UCL4U5PopumiWY','Diho'),(909,'7hJpyuLhmpawafcRfxUnlT','Bibič'),(913,'1AN5wcwNGCGfwJqABp0P6y','Sekko'),(915,'5f7VJjfbwm532GiveGC0ZK','Lil Baby'),(917,'3AlRiyjMywTVNzTcHbf9QT','Lil Kleine'),(918,'4iCzh7b2cLbHVsPOwhr8W0','JoeyAK'),(921,'7afPAbg5jb45KFUSnHIMFG','Lanek'),(922,'2o5jDhtHVPhrJdv3cEQ99Z','Tiësto'),(923,'25uiPmTg16RbhZWAqwLBy5','Charli XCX'),(924,'4O15NlyKLIASxsJ0PrXPfz','Lil Uzi Vert'),(925,'3LZZPxNDGDFVSIPqf4JuEf','Ice Spice'),(928,'09EhOOo1mFG5MNORvPQtzn','Eurosoundz'),(931,'58n40EtcUlarXICnPb9ohx','BeMelo'),(932,'7ubpSmIID5osd0LZkksfnQ','Gory'),(933,'0CEw36eWG0dYKCXOX8eUoO','Agnieszka Chylińska'),(934,'5UQaUYDQ9gRuUSJQPnaWda','Sandra S'),(935,'1DjrwkyosB44sfSdm6fT6O','club2020'),(940,'1CEONobXawu0XPgPhgTD5a','Dwa Sławy'),(941,'6f3oixxZSgRKOW2CSqOFqM','Gruby Mielzky'),(943,'0zzP72k8pbLySGH1TPUZW8','Fagata'),(951,'2YZyLoL8N0Wb9xBt1NhZWg','Kendrick Lamar'),(953,'3OFZwEYEAKMEmUheZ8TKso','Magiera'),(954,'7iZtZyCzp3LItcw1wtPI3D','Rae Sremmurd'),(957,'15UsOTVnJzReFVN1VCnxy4','XXXTENTACION'),(959,'0suD5l3wWM0EdjkhrBfUxk','Swizzy'),(960,'00o5eWNk5MqreQLbngsikb','Worek'),(961,'4z9oiedO8ugGNpfbJcg0iq','Nolyrics Beats'),(962,'5ic8bWWvZHWf0dDBi9ThNk','bambi'),(963,'4h0vqFFUqp5yFQ7K3dyJD8','Mjonszu'),(964,'365io48i1yD9KNNBbZpIK9','Qbik'),(967,'0YinUQ50QDB7ZxSCLyQ40k','Mustard'),(968,'6oMuImdp5ZcFhWP0ESe6mG','Migos'),(969,'3nFkdlSjzX9mRTtwJOzDYB','JAY-Z'),(971,'6jJ0s89eD6GaHleKKya26X','Katy Perry'),(972,'7juKTDFlPesGeWQ1GmjmOv','Silentó'),(975,'0N0d3kjwdY2h7UVuTdJGfp','Cascada'),(977,'2jLE4BoXHriQ96JagEtiDP','Lauren Bennett'),(978,'53sIBaVjXQhfH89Vu6nEGh','GoonRock'),(980,'7fObcBw9VM3x7ntWKCYl0z','Colby O\'Donis'),(1358,'0LX2VNf5w4iOHW1yyIqb74','Bedoes 2115'),(1359,'4nPxrGG7k7aEKmNLsfX4cd','White 2115'),(1360,'2FtYzWBUVhZ2vfy8S207Zf','Kuqe 2115'),(1361,'56znIsN2NyCMzIctR2xknQ','Flexxy 2115'),(1362,'71tiWMKZ5wpl6E0BdwVQza','Blacha 2115'),(1363,'0WDJa0qnagyOnMaiD26wht','Kubi Producent'),(1365,'6DAQjwwMGZ9QgqHhIkU7H0','Sentino'),(1399,'462yq5vpZnO172v3nK9ibv','Paluch'),(1401,'6kXm2YCtdUOpRYNKeKhfue','Ryan Gosling'),(1403,'19zuiWthJYU6FCqnV4mJYC','Kinny Zimmer'),(1406,'5baC8UIJpELH6bYjbeABJ3','Bandura'),(1407,'44FnIf8PhG6EQRIoENsXu3','Janusz Walczuk'),(1409,'1Fr0Md8mOOg75V07Awv1G5','TomB'),(1410,'3nRMDZRkUvf32LMdY5mJoE','Dżinold'),(1498,'4Cx5LnF4WNJIn9SSqyeq9C','bdrmm'),(1540,'0SwO7SWeDHJijQ3XNS7xEE','MGMT'),(1541,'5sWHDYs0csV6RS48xBl0tH','Two Feet');
/*!40000 ALTER TABLE `artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_song_counter`
--

DROP TABLE IF EXISTS `daily_song_counter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_song_counter` (
  `song_id` int unsigned NOT NULL AUTO_INCREMENT,
  `counter` bigint NOT NULL DEFAULT '0',
  PRIMARY KEY (`song_id`),
  CONSTRAINT `songs_song_id_foreign` FOREIGN KEY (`song_id`) REFERENCES `songs` (`song_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1054 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_song_counter`
--

LOCK TABLES `daily_song_counter` WRITE;
/*!40000 ALTER TABLE `daily_song_counter` DISABLE KEYS */;
INSERT INTO `daily_song_counter` VALUES (932,0),(933,0),(934,0),(935,0),(936,0),(937,0),(938,0),(939,0),(940,0),(941,0),(942,0),(943,0),(944,0),(945,0),(946,0),(947,0),(948,0),(949,0),(950,0),(951,0),(952,0),(953,0),(954,0),(955,0),(956,0),(957,0),(958,0),(959,0),(960,0),(961,0),(962,0),(963,0),(964,0),(965,0),(966,0),(967,0),(968,0),(969,0),(970,0),(971,0),(972,0),(973,0),(974,0),(975,0),(976,0),(977,0),(978,0),(979,0),(980,0),(981,0),(982,0),(983,0),(984,0),(985,0),(986,0),(987,0),(988,0),(989,0),(990,0),(991,0),(992,0),(993,0),(994,0),(995,0),(996,0),(997,0),(998,0),(999,0),(1000,0),(1001,0),(1002,0),(1003,0),(1004,0),(1005,0),(1006,0),(1007,0),(1008,0),(1009,0),(1010,0),(1011,0),(1012,0),(1013,0),(1014,0),(1015,0),(1016,0),(1017,0),(1018,0),(1019,0),(1020,0),(1021,0),(1022,0),(1023,0),(1024,0),(1025,0),(1026,0),(1027,0),(1028,0),(1029,0),(1030,0),(1031,0),(1032,0),(1033,0),(1034,0),(1035,0),(1036,0),(1037,0),(1038,0),(1039,0),(1040,0),(1041,0),(1042,0),(1043,0),(1044,0),(1045,0),(1046,0),(1047,0),(1048,0),(1049,0),(1050,0),(1051,0),(1052,0),(1053,0);
/*!40000 ALTER TABLE `daily_song_counter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs` (
  `song_id` int unsigned NOT NULL AUTO_INCREMENT,
  `spotify_id` varchar(24) NOT NULL,
  `song_name` varchar(255) NOT NULL,
  `added_by` varchar(255) DEFAULT NULL,
  `added_at` datetime DEFAULT NULL,
  PRIMARY KEY (`song_id`),
  UNIQUE KEY `spotify_id` (`spotify_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1054 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES (932,'0R7YVi7w41Dr9jU5vblAok','Sweat - Remix','kubadralus','2022-05-02 14:42:31'),(933,'127uq83uGFapbddqiMUKky','Sexy Bitch (feat. Akon)','kubadralus','2022-05-02 14:42:26'),(934,'41QtT8n6Sfu1wFEUKLya8L','Drink - Dirty','kubadralus','2022-05-02 14:46:34'),(935,'5s5SLh4A1UqPwTNX9Nfeji','3 króli','kubadralus','2022-05-02 14:42:13'),(936,'1FXtv58HBnJJXoQLqF5RqY','Płonę jak ognisko','kubadralus','2022-05-02 14:42:39'),(937,'1kxyZ2SpflM1ogD0B5hgfX','Can\'t Believe It (feat. Pitbull)','kubadralus','2022-05-02 14:42:20'),(938,'0OPyDgTRuIdCJ9B4bYSths','Hotel Room Service','kubadralus','2022-05-02 14:42:23'),(939,'3E6aTU15CDZVvhDfJ0Be1g','Hajs trzeba rozjebać','kubadralus','2022-05-02 14:42:17'),(940,'3rfhI32Il2hVRKDkuGeeen','Hey Baby (Drop It to the Floor) (feat. T-Pain)','kubadralus','2022-05-02 14:42:34'),(941,'0eH2eHURaXUP15D8gQlfjx','LoveGame','kubadralus','2022-05-02 14:51:12'),(942,'0p0KHvE29x9LoOsCbs25HD','Shots','kubadralus','2022-05-02 14:42:37'),(943,'4sCSUQnWQ6HJsOMjfPicdn','Danza Kuduro','kubadralus','2022-05-02 14:42:28'),(944,'6rDWCP2cWEDHpBnK2L14u5','Single Ladies','kubadralus','2022-05-02 14:42:46'),(945,'79s5XnCN4TJKTVMSmOx8Ep','Dior','kubadralus','2022-05-02 14:42:54'),(946,'63raFrC3ZwdNTE9fwmDb1g','Party Shaker - Video Edit','kubadralus','2022-05-02 14:43:14'),(947,'0F8zqM99Jiq0aSr2hXYOXx','Ona lubi pomarańcze','kubadralus','2022-05-02 14:43:52'),(948,'5OnBSGtlq0BfLG8NVedVcJ','Nie Daj Życiu Się','kubadralus','2022-05-02 14:42:52'),(949,'5hmOuIHkr2DQnIVEinfYff','House Party - Radio Edit','kubadralus','2022-05-02 14:43:16'),(950,'4qikXelSRKvoCqFcHLB2H2','Mercy','kubadralus','2022-05-02 14:48:27'),(951,'0bhn7py61O4FIAOzgjhmoV','Welcome to St. Tropez - DJ Antoine vs. Mad Mark Radio Edit','kubadralus','2022-05-02 14:43:22'),(952,'7ElF5zxOwYP4qVSWVvse3W','Break Your Heart','kubadralus','2022-05-02 14:43:28'),(953,'3C0nOe05EIt1390bVABLyN','On The Floor','kubadralus','2022-05-02 14:43:41'),(954,'1PIAwdsNMrJcr7RqUgZOvP','Robię Yeah (prod.by FRNKIE)','kubadralus','2022-05-02 14:42:43'),(955,'2JY04WbtwfYltefsImOcjg','All My People','kubadralus','2022-05-02 14:43:57'),(956,'6qfXRudT5KuBbaVlH6T7Ws','Ray Ban Vision - Casper & B. Remix','kubadralus','2022-05-02 14:43:03'),(957,'77ePeF9L2QKvKrSsWpJXBF','Suave (Kiss Me) (feat. Mohombi & Pitbull)','kubadralus','2022-05-02 14:44:34'),(958,'0O45fw2L5vsWpdsOdXwNAR','SexyBack (feat. Timbaland)','kubadralus','2022-05-02 14:44:03'),(959,'5cQrcDeXnXmJVLrM1fqJxv','Szonlover','kubadralus','2022-05-02 14:44:05'),(960,'47vY0q2TEkkPsGNWtccNlZ','NICKI','kubadralus','2022-05-02 14:44:08'),(961,'0ByMNEPAPpOR5H69DVrTNy','Don\'t Stop The Music','kubadralus','2022-05-02 14:45:17'),(962,'5l3CML2OnzfNs5RfVgbcLt','Talk Dirty (feat. 2 Chainz)','kubadralus','2022-05-02 14:44:55'),(963,'1Oenqmtbzt331Pgv0ODfS2','Outta Your Mind','kubadralus','2022-05-02 14:44:59'),(964,'4L9Dgw8nzjmSiymD83qyjq','popek pakistanskie disco','kubadralus','2022-05-02 14:45:03'),(965,'1n7omixiROWs5q6xpWiQuL','Satisfaction - Isak Original Extended','kubadralus','2022-05-02 14:45:10'),(966,'0pJV5fExkPQosiiDp4OvUj','Summer Jam','kubadralus','2022-05-02 14:45:12'),(967,'2iblMMIgSznA464mNov7A8','Don\'t Stop the Party (feat. TJR)','kubadralus','2022-05-02 14:45:21'),(968,'5pmL3RzOy3IvGFaSDi4hZL','Hangover','kubadralus','2022-05-02 14:45:26'),(969,'2s5YN9O8Qv25BjQobPHWVZ','Like A G6','kubadralus','2022-05-02 14:45:29'),(970,'40mjsnRjCpycdUw3xhS20g','GATTI','kubadralus','2022-05-02 14:45:52'),(971,'0fIffclhgJC5h8AdMMVvkp','Welcome To The Party','kubadralus','2022-05-02 14:46:00'),(972,'73xXDeBMlC5cdvWoOLWVLo','Dip (feat. Nicki Minaj) (feat. Nicki Minaj)','kubadralus','2022-05-02 14:44:50'),(973,'5qTvkDrSfvwDv6RBjjcfQr','Get Busy','kubadralus','2022-05-02 14:46:09'),(974,'0C4ejWmOTMv8vuYj85mf8m','S&M','kubadralus','2022-05-02 14:47:25'),(975,'3VOajvCUEPuuuDjmJUh5xO','Worki W Tłum','kubadralus','2022-05-02 14:46:11'),(976,'0CAfXk7DXMnon4gLudAp7J','Low (feat. T-Pain)','kubadralus','2022-05-02 14:46:21'),(977,'4VEf3UQcYsNka5kbZSoF0A','Intercontinental bajers','kubadralus','2022-05-02 14:46:23'),(978,'2OW84isCQ27lYMcGT4uNFo','I Took A Pill In Remiza','kubadralus','2022-05-02 14:47:08'),(979,'3oNKjHYfg4HAP1ivjUit9n','Jungle Girl','kubadralus','2022-05-02 14:46:37'),(980,'17WFj5Mbg9gP2NdmYgkCpd','Stonerki','kubadralus','2022-05-02 14:47:30'),(981,'30U858jspmM5gcFlCGm3Ar','Mambo (feat. Sean Paul, El Alfa, Sfera Ebbasta & Play-N-Skillz)','kubadralus','2022-05-02 14:47:37'),(982,'3eJH2nAjvNXdmPfBkALiPZ','Acapulco','kubadralus','2022-05-02 14:47:49'),(983,'0lLwj0xkoYnDUWtiMX0Jtd','Scream & Shout','kubadralus','2022-05-02 14:47:54'),(984,'6ic8OlLUNEATToEFU3xmaH','Gimme More','kubadralus','2022-05-02 14:47:58'),(985,'6gi6y1xwmVszDWkUqab1qw','OUT WEST (feat. Young Thug)','kubadralus','2022-05-02 14:48:17'),(986,'2jG3STVcZ9fjYlhXPi7nJ1','Jetlag (feat. The Plug)','kubadralus','2022-05-02 14:48:20'),(987,'7IBlBZVNt959jFh55akuwW','Łyk i buch','kubadralus','2022-05-02 14:48:24'),(988,'6LcauUZjF1eXQrgqMUecHX','Ayy Macarena','kubadralus','2022-05-02 14:48:32'),(989,'5FQazQxWUHsJ8QDaXLdFzR','Blow','kubadralus','2022-05-02 14:50:45'),(990,'7LB3ilSpX1mSMKKztNTnu2','Coupe','kubadralus','2022-05-02 14:54:17'),(991,'3rIdqj3VcQ78Szji5UKSuR','Zygzak','kubadralus','2022-05-02 14:56:39'),(992,'5rb9QrpfcKFHM1EUbSIurX','Yeah! (feat. Lil Jon & Ludacris)','kubadralus','2022-05-02 14:57:35'),(993,'3PSmflz5XrvJunj8vSKAdi','Czarny Dress','kubadralus','2022-05-02 15:00:11'),(994,'0LgdOeB2FXEWsDfZefvrkW','Jagodzianki','kubadralus','2022-05-02 15:00:55'),(995,'5D2mYZuzcgjpchVY1pmTPh','Candy Shop','kubadralus','2022-05-02 15:01:30'),(996,'275a9yzwGB6ncAW4SxY7q3','Panda','kubadralus','2022-05-02 17:41:50'),(997,'6EfBMJQwe2xLgldra6DaYp','YAYA','kubadralus','2022-05-02 15:04:08'),(998,'1XdbvPWz4lhyRBMz9cBy8b','GOOBA','kubadralus','2022-05-02 15:03:19'),(999,'4Oun2ylbjFKMPTiaSbbCih','WAP (feat. Megan Thee Stallion)','kubadralus','2022-05-02 17:43:56'),(1000,'1QV6tiMFM6fSOKOGLMHYYg','Poker Face','kubadralus','2022-05-03 12:39:41'),(1001,'5QnNZZYDoZ2lZQTGIr4at4','Sex Kaska (O Kurde Kaska)','kubadralus','2022-05-10 10:55:19'),(1002,'7g05XsuwROZFkUDNyktZdm','Puerto Bounce','kubadralus','2022-05-10 10:59:21'),(1003,'60jzFy6Nn4M0iD1d94oteF','Rude Boy','kubadralus','2022-05-13 17:36:33'),(1004,'3OcyTN8Nz3bdne5aq9mMR5','Bandyta','kubadralus','2022-05-13 17:36:48'),(1005,'0k2GOhqsrxDTAbFFSdNJjT','Temperature','kubadralus','2022-05-16 18:43:55'),(1006,'5tf6l0XZAeKtwbYFBe75Gy','Take a Shot and Make a TikTok','kubadralus','2022-05-16 18:44:23'),(1007,'7w8SYlPLA9bqj7vRHvYNDz','Alive (with Offset & 2 Chainz)','kubadralus','2022-05-16 20:57:44'),(1008,'7ApeFeWYcnTTGOpo5b9Yx6','La Manga','kubadralus','2022-05-18 10:07:05'),(1009,'4QNpBfC0zvjKqPJcyqBy9W','Give Me Everything (feat. Ne-Yo, Afrojack & Nayer)','kubadralus','2022-05-18 10:07:34'),(1010,'6yPYf2WsJWfbUM6f63MwQq','Bumpy Ride','kubadralus','2022-05-19 09:46:45'),(1011,'38ryCMNFOZ6GW5udIFnQI7','PIĄTEK WIECZÓR','kubadralus','2022-05-20 19:55:18'),(1012,'4OAPnWJ3J5w4c4IBLh2chn','BOMBÓN','kubadralus','2022-05-26 19:18:38'),(1013,'0S5otf3yhH2NIozxJPJTeV','Let\'s Get Ridiculous','kubadralus','2022-06-17 20:36:00'),(1014,'4Xq0cVrd0JDXQ0p3mlKAr3','KOKAINA','kubadralus','2022-06-30 16:14:51'),(1015,'1QjaX3Jp5kbDDorjL9ktRQ','Rundki (feat. Diho, Alberto & Bibič)','kubadralus','2022-07-13 18:56:28'),(1016,'5t82x7Pp2y5ji2R1BpiOik','Dzielny Pacjent','kubadralus','2022-07-15 19:00:53'),(1017,'7lcI4X8RZxK4zIknJcwpBq','Bussin','kubadralus','2022-07-15 19:10:17'),(1018,'3GJW3WLsbqcP0HAFlIvzAC','Kapitan','kubadralus','2022-07-22 10:01:06'),(1019,'50xUHMCmsbBOp6aaihNYyg','Jongens Van Plein','kubadralus','2022-08-07 13:19:44'),(1020,'2ZRdQMMKtmPLdYp9aP5cK5','Hawk Em','kubadralus','2022-09-23 14:54:37'),(1021,'7n7QAwwFJG7jOjxgACW1XC','Grill u Gawrona','kubadralus','2022-09-21 20:08:42'),(1022,'3Z7CaxQkqbIs1rewKi6v4W','Hot In It','kubadralus','2022-09-23 14:54:43'),(1023,'4FyesJzVpA39hbYvcseO2d','Just Wanna Rock','kubadralus','2022-11-18 19:46:16'),(1024,'1jOgJN75btuUONIdf57vHz','Munch (Feelin’ U)','kubadralus','2022-12-28 16:47:19'),(1025,'4nv5o5Xo4ySBaIVnXr75Xs','Do Tanca','kubadralus','2022-12-28 18:13:42'),(1026,'17vGPZ5EsdvtgAOCD4FLWI','AP - Music from the film Boogie','kubadralus','2023-01-15 19:57:30'),(1027,'09m29we7x9tgxyo6f3OQ87','Discopolo','kubadralus','2023-01-15 19:58:03'),(1028,'6A6537BwTdiRefKxjYyYAD','Nie mogę cię zapomnieć - Radio Edit','kubadralus','2023-02-10 17:44:07'),(1029,'65HEZXKmXqSQlvyWFUyagn','Big Klamoty','kubadralus','2023-02-05 13:24:47'),(1030,'0KMDkQbcglNudXuynwKMs6','Malibu Barbie','kubadralus','2023-02-05 13:27:17'),(1031,'1zwN0wYkc1uGVJHmcNqvBF','Wielka szkoda','kubadralus','2023-03-13 21:20:51'),(1032,'6Yq2Dnb5Gre9mAT0TEDiZx','No weź','kubadralus','2023-04-29 10:07:31'),(1033,'2VOomzT6VavJOGBeySqaMc','Disturbia','kubadralus','2023-04-29 10:10:59'),(1034,'7KXjTSCq5nL1LoYtL7XAwS','HUMBLE.','kubadralus','2023-04-29 10:11:18'),(1035,'1e5AS7EC7VnUo40me9YNwV','I To Jest Fakt','kubadralus','2023-04-29 10:11:37'),(1036,'1Ser4X0TKttOvo8bgdytTP','Come Get Her','kubadralus','2023-04-29 10:15:00'),(1037,'3gG4bxTKqZgX199TF22Cko','Sexoholik','kubadralus','2023-04-29 10:18:26'),(1038,'7yvfHQ12Q0sFPLST4M0x7Z','Bestia - Bestia (prod. Worek)','kubadralus','2023-04-29 10:19:15'),(1039,'7floNISpH8VF4z4459Qo18','Look At Me!','kubadralus','2023-05-01 07:52:28'),(1040,'1ZZ7uFD6pS1Rt3ELtMqsSl','SPRZEDAŁEM SIĘ','kubadralus','2023-05-01 07:52:39'),(1041,'0Mh7nzWn5BHJSenmaUSEt6','IRL','kubadralus','2023-05-01 07:53:21'),(1042,'0OsGuRyi1w0cd6hCw1qb2r','4 Pory Roku','kubadralus','2023-05-01 07:54:25'),(1043,'0e9qii2fpZNl6UStkD8vFi','Pogo','kubadralus','2023-05-01 07:54:31'),(1044,'3j84U36KvLeXNDPv4t5pI8','Pure Water (with Migos)','kubadralus','2023-05-01 07:58:04'),(1045,'4Li2WHPkuyCdtmokzW2007','Ni**as In Paris','kubadralus','2023-05-01 08:01:35'),(1046,'50r1EUDpmSZRPo5aIZpmWi','E.T.','kubadralus','2023-05-03 14:35:32'),(1047,'5RIVoVdkDLEygELLCniZFr','Watch Me (Whip / Nae Nae)','kubadralus','2023-05-03 14:36:22'),(1048,'3f7gYMirBEKuc57218BjOY','California Gurls','kubadralus','2023-05-04 14:13:58'),(1049,'5aEqcblO0Z6JloFJXtxyhe','Everytime We Touch','kubadralus','2023-05-06 15:46:19'),(1050,'4650WGL6InVqP7YN5POqIz','Party Rock Anthem','kubadralus','2023-05-06 15:47:04'),(1051,'1dzQoRqT5ucxXVaAhTcT0J','Just Dance','kubadralus','2023-07-01 11:45:48'),(1052,'7lONOPBZxV4eo3zUijvb1b','You\'re Ma Cherie - DJ Antoine vs. Mad Mark 2k13 Radio Edit','kubadralus','2023-07-01 11:46:24'),(1053,'61FwUf89hKEIsjUDtIPRoH','JUMPIN','kubadralus','2023-07-15 10:22:07');
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `insert_daily_song_counter` AFTER INSERT ON `songs` FOR EACH ROW BEGIN
    -- Dodajemy nowy rekord do tabeli daily_song_counter z wartością counter = 0
    INSERT INTO daily_song_counter (song_id, counter)
    VALUES (NEW.song_id, 0);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `songs_by_artists`
--

DROP TABLE IF EXISTS `songs_by_artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs_by_artists` (
  `artist_id` int unsigned NOT NULL,
  `song_id` int unsigned NOT NULL,
  PRIMARY KEY (`artist_id`,`song_id`),
  KEY `songs_by_artists_ibfk_2` (`song_id`),
  CONSTRAINT `songs_by_artists_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`artist_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `songs_by_artists_ibfk_2` FOREIGN KEY (`song_id`) REFERENCES `songs` (`song_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs_by_artists`
--

LOCK TABLES `songs_by_artists` WRITE;
/*!40000 ALTER TABLE `songs_by_artists` DISABLE KEYS */;
INSERT INTO `songs_by_artists` VALUES (737,932),(738,932),(739,932),(740,932),(738,933),(742,933),(743,934),(744,934),(745,935),(746,935),(747,936),(748,936),(749,936),(750,937),(751,937),(751,938),(753,939),(751,940),(755,940),(756,941),(743,942),(744,942),(759,943),(760,943),(761,944),(762,944),(763,945),(764,946),(765,946),(766,947),(766,948),(768,949),(769,949),(770,949),(771,949),(772,950),(773,950),(774,950),(775,950),(768,951),(777,951),(778,951),(779,952),(751,953),(780,953),(782,954),(783,954),(784,955),(785,956),(786,956),(787,956),(788,957),(789,958),(790,958),(791,959),(792,960),(793,960),(794,961),(775,962),(795,962),(743,963),(744,963),(746,964),(800,965),(801,965),(764,966),(803,966),(751,967),(805,967),(750,968),(779,968),(808,969),(809,969),(810,969),(763,970),(811,970),(813,970),(763,971),(815,972),(816,972),(817,973),(794,974),(819,975),(820,975),(821,975),(822,975),(750,976),(755,976),(825,977),(826,977),(827,978),(828,978),(829,979),(830,979),(829,980),(832,980),(817,981),(833,981),(834,981),(836,981),(837,981),(838,981),(795,982),(840,983),(841,983),(841,984),(811,985),(813,985),(845,985),(783,986),(847,986),(848,986),(849,986),(828,987),(850,987),(852,987),(853,987),(815,988),(855,989),(763,990),(857,991),(858,991),(743,992),(859,992),(861,992),(862,993),(863,993),(864,993),(783,994),(862,994),(867,995),(868,995),(869,996),(870,997),(870,998),(872,999),(873,999),(756,1000),(875,1001),(830,1002),(864,1002),(878,1002),(879,1002),(794,1003),(881,1004),(882,1004),(817,1005),(743,1006),(750,1006),(884,1006),(743,1007),(775,1007),(888,1007),(329,1008),(890,1008),(891,1008),(751,1009),(788,1009),(894,1009),(895,1009),(751,1010),(897,1010),(829,1011),(858,1011),(743,1012),(836,1012),(901,1012),(904,1013),(905,1014),(783,1015),(890,1015),(907,1015),(909,1015),(819,1016),(820,1016),(881,1016),(913,1016),(816,1017),(915,1017),(793,1018),(917,1019),(918,1019),(763,1020),(826,1021),(921,1021),(922,1022),(923,1022),(924,1023),(925,1024),(783,1025),(830,1025),(928,1025),(763,1026),(864,1027),(931,1027),(932,1027),(933,1028),(934,1029),(311,1030),(819,1030),(821,1030),(829,1030),(935,1030),(940,1030),(941,1030),(907,1031),(943,1031),(311,1032),(819,1032),(820,1032),(829,1032),(882,1032),(935,1032),(794,1033),(951,1034),(819,1035),(953,1035),(954,1036),(830,1037),(820,1038),(957,1039),(819,1040),(959,1040),(960,1040),(961,1040),(962,1041),(963,1041),(964,1042),(819,1043),(864,1043),(967,1044),(968,1044),(772,1045),(969,1045),(971,1046),(972,1047),(737,1048),(971,1048),(975,1049),(744,1050),(977,1050),(978,1050),(756,1051),(980,1051),(751,1052),(768,1052),(743,1053),(751,1053);
/*!40000 ALTER TABLE `songs_by_artists` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-02  2:20:04
