PGDMP     *                    {            Hand-A-Game    15.1    15.1 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16415    Hand-A-Game    DATABASE     �   CREATE DATABASE "Hand-A-Game" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Canada.1252';
    DROP DATABASE "Hand-A-Game";
                postgres    false            �            1259    16423 
   Plataforma    TABLE     &   CREATE TABLE public."Plataforma" (
);
     DROP TABLE public."Plataforma";
       public         heap    postgres    false            �            1259    16416    usuario    TABLE     �   CREATE TABLE public.usuario (
    id integer NOT NULL,
    nome character varying(100),
    contato character varying(100),
    cidade character varying(100),
    email character varying(100),
    hashsehnha character varying(100)
);
    DROP TABLE public.usuario;
       public         heap    postgres    false            �          0    16423 
   Plataforma 
   TABLE DATA           &   COPY public."Plataforma"  FROM stdin;
    public          postgres    false    215   a       �          0    16416    usuario 
   TABLE DATA           O   COPY public.usuario (id, nome, contato, cidade, email, hashsehnha) FROM stdin;
    public          postgres    false    214   ~       i           2606    16422    usuario usuario_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    214            �      x������ � �      �      x������ � �     