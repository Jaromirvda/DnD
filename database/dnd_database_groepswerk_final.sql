PGDMP  5    *                 |            dnd_groepswerk    16.0    16.0                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16516    dnd_groepswerk    DATABASE     �   CREATE DATABASE dnd_groepswerk WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Dutch_Belgium.1252';
    DROP DATABASE dnd_groepswerk;
                postgres    false                      0    16532    boss 
   TABLE DATA           `   COPY public.boss (boss_id, boss_name, boss_damage, boss_hp, boss_speed, boss_armer) FROM stdin;
    public          postgres    false    220   �                 0    16575    karakter_classes 
   TABLE DATA           �   COPY public.karakter_classes (class_id, class_hp, class_damage, class_speed, class_name, magic_damage, true_damage, stealth_damage, class_armer) FROM stdin;
    public          postgres    false    223   �                 0    16525    monster_tier1 
   TABLE DATA           {   COPY public.monster_tier1 (monster_id, monster_name, monster_damage, monster_hp, monster_speed, monster_armer) FROM stdin;
    public          postgres    false    218   V                 0    16630    monster_tier2 
   TABLE DATA           {   COPY public.monster_tier2 (monster_id, monster_name, monster_damage, monster_hp, monster_speed, monster_armer) FROM stdin;
    public          postgres    false    225   �       
          0    16518    spelers 
   TABLE DATA           O   COPY public.spelers (spelers_id, karakter_class_id, karakter_name) FROM stdin;
    public          postgres    false    216   �                   0    0    boss_boss_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.boss_boss_id_seq', 3, true);
          public          postgres    false    219            !           0    0    karakter_classes_class_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.karakter_classes_class_id_seq', 3, true);
          public          postgres    false    222            "           0    0    monster_monster_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.monster_monster_id_seq', 6, true);
          public          postgres    false    217            #           0    0    monster_tier2_monster_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.monster_tier2_monster_id_seq', 3, true);
          public          postgres    false    224            $           0    0    spelers_karakter_class_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.spelers_karakter_class_id_seq', 1, false);
          public          postgres    false    221            %           0    0    spelers_spelers_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.spelers_spelers_id_seq', 1, false);
          public          postgres    false    215               J   x�3�L)JL���44�42�4!.#����D�Ĥ��ĒL��)��H�)�1gRjF~NJjH�(j�i����� ��d         H   x�3�44�4�4��MLO�4�4 Bc.#Ns ۜ3��8�83,j�i�e�ih
Tk�Y����� i1����� "�1         @   x�3�L�O����4�44 F\F�%E�99�F���@˘3=13�D�(����ʔӘ+F��� � �         G   x�3�,K�-�,JUHJ,�4�44�44�4�2��H��Q��/�K� ��sqs�'f敀���@3�=... ax�      
      x������ � �     