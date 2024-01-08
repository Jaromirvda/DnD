PGDMP                       |            dnd_groepswerk    16.0    16.0 /               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16516    dnd_groepswerk    DATABASE     �   CREATE DATABASE dnd_groepswerk WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Dutch_Belgium.1252';
    DROP DATABASE dnd_groepswerk;
                postgres    false            �            1255    16642 
   add_boss() 	   PROCEDURE     �  CREATE PROCEDURE public.add_boss()
    LANGUAGE sql
    AS $_$CREATE OR REPLACE PROCEDURE add_boss(
    boss_name character varying,
    boss_damage smallint,
    boss_hp smallint,
    boss_speed smallint,
    boss_armor smallint
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO boss(boss_name, boss_damage, boss_hp, boss_speed, boss_armor)
    VALUES (boss_name, boss_damage, boss_hp, boss_speed, boss_armor);
END;
$$;
$_$;
 "   DROP PROCEDURE public.add_boss();
       public          postgres    false            �            1255    16640    add_monstertier1() 	   PROCEDURE     �  CREATE PROCEDURE public.add_monstertier1()
    LANGUAGE sql
    AS $_$CREATE OR REPLACE PROCEDURE add_monster_tier1(
    monster_name character varying,
    monster_damage smallint,
    monster_hp smallint,
    monster_speed smallint,
    monster_armor smallint
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO monster_tier1(monster_name, monster_damage, monster_hp, monster_speed, monster_armor)
    VALUES (monster_name, monster_damage, monster_hp, monster_speed, monster_armor);
END;
$$;
$_$;
 *   DROP PROCEDURE public.add_monstertier1();
       public          postgres    false            �            1255    16641    add_monstertier2() 	   PROCEDURE     �  CREATE PROCEDURE public.add_monstertier2()
    LANGUAGE sql
    AS $_$CREATE OR REPLACE PROCEDURE add_monster_tier2(
    monster_name character varying,
    monster_damage smallint,
    monster_hp smallint,
    monster_speed smallint,
    monster_armor smallint
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO monster_tier2(monster_name, monster_damage, monster_hp, monster_speed, monster_armor)
    VALUES (monster_name, monster_damage, monster_hp, monster_speed, monster_armor);
END;
$$;
$_$;
 *   DROP PROCEDURE public.add_monstertier2();
       public          postgres    false            �            1259    16532    boss    TABLE     �   CREATE TABLE public.boss (
    boss_id integer NOT NULL,
    boss_name character varying(20) NOT NULL,
    boss_damage smallint NOT NULL,
    boss_hp smallint NOT NULL,
    boss_speed smallint NOT NULL,
    boss_armer smallint
);
    DROP TABLE public.boss;
       public         heap    postgres    false            �            1259    16531    boss_boss_id_seq    SEQUENCE     �   CREATE SEQUENCE public.boss_boss_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.boss_boss_id_seq;
       public          postgres    false    220                       0    0    boss_boss_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.boss_boss_id_seq OWNED BY public.boss.boss_id;
          public          postgres    false    219            �            1259    16575    karakter_classes    TABLE     L  CREATE TABLE public.karakter_classes (
    class_id integer NOT NULL,
    class_hp smallint DEFAULT 15 NOT NULL,
    class_damage smallint NOT NULL,
    class_speed smallint NOT NULL,
    class_name character varying(20),
    magic_damage smallint,
    true_damage smallint,
    stealth_damage smallint,
    class_armer smallint
);
 $   DROP TABLE public.karakter_classes;
       public         heap    postgres    false            �            1259    16574    karakter_classes_class_id_seq    SEQUENCE     �   CREATE SEQUENCE public.karakter_classes_class_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.karakter_classes_class_id_seq;
       public          postgres    false    223                       0    0    karakter_classes_class_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.karakter_classes_class_id_seq OWNED BY public.karakter_classes.class_id;
          public          postgres    false    222            �            1259    16525    monster_tier1    TABLE       CREATE TABLE public.monster_tier1 (
    monster_id integer NOT NULL,
    monster_name character varying(20) NOT NULL,
    monster_damage smallint NOT NULL,
    monster_hp smallint NOT NULL,
    monster_speed smallint NOT NULL,
    monster_armer smallint
);
 !   DROP TABLE public.monster_tier1;
       public         heap    postgres    false            �            1259    16524    monster_monster_id_seq    SEQUENCE     �   CREATE SEQUENCE public.monster_monster_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.monster_monster_id_seq;
       public          postgres    false    218                       0    0    monster_monster_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.monster_monster_id_seq OWNED BY public.monster_tier1.monster_id;
          public          postgres    false    217            �            1259    16630    monster_tier2    TABLE     �   CREATE TABLE public.monster_tier2 (
    monster_id integer NOT NULL,
    monster_name character varying(20) NOT NULL,
    monster_damage smallint,
    monster_hp smallint,
    monster_speed smallint,
    monster_armer smallint
);
 !   DROP TABLE public.monster_tier2;
       public         heap    postgres    false            �            1259    16629    monster_tier2_monster_id_seq    SEQUENCE     �   CREATE SEQUENCE public.monster_tier2_monster_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.monster_tier2_monster_id_seq;
       public          postgres    false    225                       0    0    monster_tier2_monster_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.monster_tier2_monster_id_seq OWNED BY public.monster_tier2.monster_id;
          public          postgres    false    224            �            1259    16518    spelers    TABLE     �   CREATE TABLE public.spelers (
    spelers_id integer NOT NULL,
    karakter_class_id integer NOT NULL,
    karakter_name character varying(20) NOT NULL
);
    DROP TABLE public.spelers;
       public         heap    postgres    false            �            1259    16538    spelers_karakter_class_id_seq    SEQUENCE     �   CREATE SEQUENCE public.spelers_karakter_class_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.spelers_karakter_class_id_seq;
       public          postgres    false    216                       0    0    spelers_karakter_class_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.spelers_karakter_class_id_seq OWNED BY public.spelers.karakter_class_id;
          public          postgres    false    221            �            1259    16517    spelers_spelers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.spelers_spelers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.spelers_spelers_id_seq;
       public          postgres    false    216                       0    0    spelers_spelers_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.spelers_spelers_id_seq OWNED BY public.spelers.spelers_id;
          public          postgres    false    215            k           2604    16535    boss boss_id    DEFAULT     l   ALTER TABLE ONLY public.boss ALTER COLUMN boss_id SET DEFAULT nextval('public.boss_boss_id_seq'::regclass);
 ;   ALTER TABLE public.boss ALTER COLUMN boss_id DROP DEFAULT;
       public          postgres    false    220    219    220            l           2604    16578    karakter_classes class_id    DEFAULT     �   ALTER TABLE ONLY public.karakter_classes ALTER COLUMN class_id SET DEFAULT nextval('public.karakter_classes_class_id_seq'::regclass);
 H   ALTER TABLE public.karakter_classes ALTER COLUMN class_id DROP DEFAULT;
       public          postgres    false    223    222    223            j           2604    16528    monster_tier1 monster_id    DEFAULT     ~   ALTER TABLE ONLY public.monster_tier1 ALTER COLUMN monster_id SET DEFAULT nextval('public.monster_monster_id_seq'::regclass);
 G   ALTER TABLE public.monster_tier1 ALTER COLUMN monster_id DROP DEFAULT;
       public          postgres    false    217    218    218            n           2604    16633    monster_tier2 monster_id    DEFAULT     �   ALTER TABLE ONLY public.monster_tier2 ALTER COLUMN monster_id SET DEFAULT nextval('public.monster_tier2_monster_id_seq'::regclass);
 G   ALTER TABLE public.monster_tier2 ALTER COLUMN monster_id DROP DEFAULT;
       public          postgres    false    224    225    225            h           2604    16521    spelers spelers_id    DEFAULT     x   ALTER TABLE ONLY public.spelers ALTER COLUMN spelers_id SET DEFAULT nextval('public.spelers_spelers_id_seq'::regclass);
 A   ALTER TABLE public.spelers ALTER COLUMN spelers_id DROP DEFAULT;
       public          postgres    false    215    216    216            i           2604    16539    spelers karakter_class_id    DEFAULT     �   ALTER TABLE ONLY public.spelers ALTER COLUMN karakter_class_id SET DEFAULT nextval('public.spelers_karakter_class_id_seq'::regclass);
 H   ALTER TABLE public.spelers ALTER COLUMN karakter_class_id DROP DEFAULT;
       public          postgres    false    221    216                      0    16532    boss 
   TABLE DATA           `   COPY public.boss (boss_id, boss_name, boss_damage, boss_hp, boss_speed, boss_armer) FROM stdin;
    public          postgres    false    220   �;                 0    16575    karakter_classes 
   TABLE DATA           �   COPY public.karakter_classes (class_id, class_hp, class_damage, class_speed, class_name, magic_damage, true_damage, stealth_damage, class_armer) FROM stdin;
    public          postgres    false    223   <                 0    16525    monster_tier1 
   TABLE DATA           {   COPY public.monster_tier1 (monster_id, monster_name, monster_damage, monster_hp, monster_speed, monster_armer) FROM stdin;
    public          postgres    false    218   l<                 0    16630    monster_tier2 
   TABLE DATA           {   COPY public.monster_tier2 (monster_id, monster_name, monster_damage, monster_hp, monster_speed, monster_armer) FROM stdin;
    public          postgres    false    225   �<       
          0    16518    spelers 
   TABLE DATA           O   COPY public.spelers (spelers_id, karakter_class_id, karakter_name) FROM stdin;
    public          postgres    false    216   =                   0    0    boss_boss_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.boss_boss_id_seq', 3, true);
          public          postgres    false    219            !           0    0    karakter_classes_class_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.karakter_classes_class_id_seq', 3, true);
          public          postgres    false    222            "           0    0    monster_monster_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.monster_monster_id_seq', 6, true);
          public          postgres    false    217            #           0    0    monster_tier2_monster_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.monster_tier2_monster_id_seq', 3, true);
          public          postgres    false    224            $           0    0    spelers_karakter_class_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.spelers_karakter_class_id_seq', 1, false);
          public          postgres    false    221            %           0    0    spelers_spelers_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.spelers_spelers_id_seq', 1, false);
          public          postgres    false    215            t           2606    16537    boss boss_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.boss
    ADD CONSTRAINT boss_pkey PRIMARY KEY (boss_id);
 8   ALTER TABLE ONLY public.boss DROP CONSTRAINT boss_pkey;
       public            postgres    false    220            v           2606    16581 &   karakter_classes karakter_classes_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.karakter_classes
    ADD CONSTRAINT karakter_classes_pkey PRIMARY KEY (class_id);
 P   ALTER TABLE ONLY public.karakter_classes DROP CONSTRAINT karakter_classes_pkey;
       public            postgres    false    223            r           2606    16530    monster_tier1 monster_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.monster_tier1
    ADD CONSTRAINT monster_pkey PRIMARY KEY (monster_id);
 D   ALTER TABLE ONLY public.monster_tier1 DROP CONSTRAINT monster_pkey;
       public            postgres    false    218            x           2606    16635     monster_tier2 monster_tier2_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.monster_tier2
    ADD CONSTRAINT monster_tier2_pkey PRIMARY KEY (monster_id);
 J   ALTER TABLE ONLY public.monster_tier2 DROP CONSTRAINT monster_tier2_pkey;
       public            postgres    false    225            p           2606    16523    spelers spelers_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.spelers
    ADD CONSTRAINT spelers_pkey PRIMARY KEY (spelers_id);
 >   ALTER TABLE ONLY public.spelers DROP CONSTRAINT spelers_pkey;
       public            postgres    false    216            y           2606    16582 &   spelers spelers_karakter_class_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.spelers
    ADD CONSTRAINT spelers_karakter_class_id_fkey FOREIGN KEY (karakter_class_id) REFERENCES public.karakter_classes(class_id) NOT VALID;
 P   ALTER TABLE ONLY public.spelers DROP CONSTRAINT spelers_karakter_class_id_fkey;
       public          postgres    false    216    223    4726               J   x�3�L)JL���44�42�4!.#����D�Ĥ��ĒL��)��H�)�1gRjF~NJjH�(j�i����� ��d         H   x�3�44�4�4��MLO�4�4 Bc.#Ns ۜ3��8�83,j�i�e�ih
Tk�Y����� i1����� "�1         @   x�3�L�O����4�44 F\F�%E�99�F���@˘3=13�D�(����ʔӘ+F��� � �         G   x�3�,K�-�,JUHJ,�4�44�44�4�2��H��Q��/�K� ��sqs�'f敀���@3�=... ax�      
      x������ � �     