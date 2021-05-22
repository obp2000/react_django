--
-- PostgreSQL database dump
--

-- Dumped from database version 10.16 (Ubuntu 10.16-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.16 (Ubuntu 10.16-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: ar_internal_metadata; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ar_internal_metadata (
    key character varying NOT NULL,
    value character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.ar_internal_metadata OWNER TO postgres;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: cities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cities (
    pindex character varying DEFAULT ''::character varying NOT NULL,
    city character varying(80) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.cities OWNER TO postgres;

--
-- Name: cities1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cities1 (
    city character varying,
    pindex character varying
);


ALTER TABLE public.cities1 OWNER TO postgres;

--
-- Name: customers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customers (
    id integer NOT NULL,
    nick character varying,
    name character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    pindex character varying,
    address character varying
);


ALTER TABLE public.customers OWNER TO postgres;

--
-- Name: customers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.customers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.customers_id_seq OWNER TO postgres;

--
-- Name: customers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.customers_id_seq OWNED BY public.customers.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: knox_authtoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.knox_authtoken (
    digest character varying(128) NOT NULL,
    salt character varying(16) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    expiry timestamp with time zone,
    token_key character varying(8) NOT NULL
);


ALTER TABLE public.knox_authtoken OWNER TO postgres;

--
-- Name: order_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.order_items (
    id integer NOT NULL,
    order_id integer,
    product_id integer,
    amount numeric,
    price numeric,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.order_items OWNER TO postgres;

--
-- Name: order_items_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_items_id_seq OWNER TO postgres;

--
-- Name: order_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_items_id_seq OWNED BY public.order_items.id;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    id integer NOT NULL,
    customer_id integer,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    post_cost integer,
    packet integer,
    delivery_type integer,
    address character varying,
    gift character varying
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_id_seq OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;


--
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posts_id_seq OWNER TO postgres;

--
-- Name: posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id integer NOT NULL,
    name character varying NOT NULL,
    price integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    weight numeric,
    width integer,
    density integer,
    dollar_price numeric,
    dollar_rate numeric,
    width_shop integer,
    density_shop integer,
    weight_for_count integer,
    length_for_count numeric DEFAULT 1.0,
    price_pre integer,
    image character varying
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: schema_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.schema_migrations (
    version character varying NOT NULL
);


ALTER TABLE public.schema_migrations OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    provider character varying DEFAULT 'email'::character varying NOT NULL,
    uid character varying DEFAULT ''::character varying NOT NULL,
    encrypted_password character varying DEFAULT ''::character varying NOT NULL,
    reset_password_token character varying,
    reset_password_sent_at timestamp without time zone,
    remember_created_at timestamp without time zone,
    sign_in_count integer DEFAULT 0 NOT NULL,
    current_sign_in_at timestamp without time zone,
    last_sign_in_at timestamp without time zone,
    current_sign_in_ip character varying,
    last_sign_in_ip character varying,
    confirmation_token character varying,
    confirmed_at timestamp without time zone,
    confirmation_sent_at timestamp without time zone,
    unconfirmed_email character varying,
    name character varying,
    nickname character varying,
    image character varying,
    email character varying,
    tokens json,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: customers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers ALTER COLUMN id SET DEFAULT nextval('public.customers_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Name: order_items id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items ALTER COLUMN id SET DEFAULT nextval('public.order_items_id_seq'::regclass);


--
-- Name: orders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Name: posts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: ar_internal_metadata; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ar_internal_metadata (key, value, created_at, updated_at) FROM stdin;
environment	development	2019-12-02 20:06:54.90977	2019-12-02 20:06:54.90977
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add auth token	9	add_authtoken
26	Can change auth token	9	change_authtoken
27	Can delete auth token	9	delete_authtoken
28	Can view auth token	9	view_authtoken
29	Can add site	15	add_site
30	Can change site	15	change_site
31	Can delete site	15	delete_site
32	Can view site	15	view_site
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$180000$z8D57OpouN1x$OQ5QVDuz/RIpw3n1+I4RB05VlD1X6k8FAI2WgTGx1+I=	\N	f	John			john@example.com	f	t	2020-04-03 16:55:29.38383+00
4	pbkdf2_sha256$180000$1N7pFO4OKgTf$tqiQM/QhWHzjqSkfRoGByYoMzpxP13af5OLRRIQuUMo=	\N	f	test2			test2@test.com	f	t	2020-04-06 20:07:59.664856+00
5	pbkdf2_sha256$180000$vF5qvl7qepBy$48P4L0JQUuXAM0O6onruIXaol3Fbmui9l9moBEw+OP8=	\N	f	test3			test3@test.com	f	t	2020-04-06 20:09:30.31453+00
6	pbkdf2_sha256$180000$Z4ntER7kJjyX$kT4JAn/GRUQvG/VFTOm4Xr8Oz8/gBx1WznvXohBIQXs=	\N	f	test4			test4@test.com	f	t	2020-04-06 20:26:06.210706+00
3	pbkdf2_sha256$180000$hjr2BGsrSgyJ$En/tMzFEUC2C8bpOukjljWVt4mU0X4EkQfnfSGOwwTs=	2020-04-07 19:59:05.270279+00	f	test1			test1@test.com	f	t	2020-04-06 18:46:22.969107+00
7	pbkdf2_sha256$180000$arT9kmRPwYjt$y3uQsEMHix/TXLPxJ5TvEcc6DFoee/e9j0gkQ+KgOmk=	\N	f	test5			test5@test.com	f	t	2020-04-08 20:07:06.09753+00
8	pbkdf2_sha256$180000$irHmPM1KqOLK$wPy4soajLqMsGJsJvDjBY6IPTU3qIR0aLEErmVLZtAE=	\N	f	test6			test6@test.com	f	t	2020-04-08 20:09:27.887323+00
9	pbkdf2_sha256$180000$OmDWAXt3Vrx6$rxzs3w9BAjDvN/HwbVobW3C9PizNicOU6zQT0ijxRpg=	\N	f	test			test7@test.com	f	t	2020-05-03 21:36:57.078577+00
10	pbkdf2_sha256$180000$hoJ1EHZcjOxH$gtjUgNKIsSt/uZZXrPnV+h3tN6nCZ6R15+p3btnhogQ=	2020-12-16 18:05:35.166995+00	f	oleg_test			obp2000@example.com	f	t	2020-11-29 18:57:42.611403+00
1	pbkdf2_sha256$216000$sdXdWRKbcZgR$BvI73bSdzcTNUhn091mFE9dKePOsOGSwkEF7OQ5tjmg=	2021-01-08 16:24:52.596894+00	t	oleg			obp2000@mail.ru	t	t	2019-12-08 18:25:13.191859+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: cities; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cities (pindex, city) FROM stdin;
440000	Саратов
628002	ХМАО-Югра, Тюменская обл., Ханты-Мансийск
153000	Иваново
101000	Москва
\.


--
-- Data for Name: cities1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cities1 (city, pindex) FROM stdin;
\.


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customers (id, nick, name, created_at, updated_at, pindex, address) FROM stdin;
28	Лариса Черкашина	Черкашина Лариса Евгеньевна	2020-11-25 00:44:59.384708	2021-01-08 20:31:13.085312	628002	пер. Курортный, д.5  тел. 89028147063
26	zvzvxzvzxv	\N	2020-11-25 00:38:28.773977	2020-11-25 00:38:28.774027	\N	\N
27	мпвыпвыпывп	\N	2020-11-25 00:40:14.356189	2020-11-25 00:40:14.356236	\N	\N
29	gssdgsdg	\N	2020-11-25 00:48:03.143178	2020-11-25 00:48:03.143284	\N	\N
30	vxzvxzvxzv	\N	2020-11-25 00:49:34.839183	2020-11-25 00:49:34.83922	\N	\N
6	test2	test2	2020-02-05 05:42:31.869265	2020-09-15 22:52:20.640196	153000	вввввввввввввв
17	test2	test2	2020-11-06 16:56:33.255164	2020-11-06 16:56:33.255202	153000	test2
22	еуые4	44444	2020-11-06 17:46:29.856811	2020-11-06 17:46:29.856873	440000	кекунукнкун
19	Новый ник	dddd	2020-11-06 17:15:38.105218	2020-11-07 19:22:28.087076	153000	\N
9	Олег	Петрущенко Олег Борисович	2011-11-09 08:00:00	2021-03-03 19:53:54.634755	153000	пр.Строителей 16-14
18	test2	test2	2020-11-06 17:15:05.23282	2021-03-03 21:12:01.016219	153000	test2
8	obp2000	Петрущенко Олег Борисович	2020-02-13 12:52:00	2021-03-03 21:12:55.382925	101000	пр.Строителей
21	test2	test3	2020-11-06 17:19:17.497232	2021-03-13 20:58:51.188748	101000	\N
1	Nick1111	Name1	2020-01-27 11:22:41.961692	2021-03-13 20:59:10.557162	101000	gggggggj
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2019-12-20 19:26:53.218503+00	1	Customer object (1)	1	[{"added": {}}]	8	1
2	2019-12-20 19:28:12.716754+00	2	Customer object (2)	1	[{"added": {}}]	8	1
3	2019-12-20 19:37:42.548286+00	3	nick2 name2	1	[{"added": {}}]	8	1
4	2020-11-07 15:13:12.532147+00	19	dddммммм (dddd)	2	[{"changed": {"fields": ["\\u0413\\u043e\\u0440\\u043e\\u0434"]}}]	11	1
5	2020-11-27 21:35:39.978931+00	25	test355yyy	2	[{"changed": {"fields": ["Image"]}}]	14	1
6	2021-01-08 16:27:04.937925+00	628002	ХМАО-Югра, Тюменская обл, Ханты-Мансийск,	1	[{"added": {}}]	10	1
7	2021-01-08 16:27:33.425013+00	628002	ХМАО-Югра, Тюменская обл., Ханты-Мансийск	2	[{"changed": {"fields": ["Name"]}}]	10	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	react_django_api	product
8	react_django_api	customer
9	knox	authtoken
10	city	city
11	customer	customer
12	order	order
13	order_item	orderitem
14	product	product
15	sites	site
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-12-02 20:53:37.141854+00
2	auth	0001_initial	2019-12-02 20:53:37.760341+00
3	admin	0001_initial	2019-12-02 20:53:38.690061+00
4	admin	0002_logentry_remove_auto_add	2019-12-02 20:53:38.838059+00
5	admin	0003_logentry_add_action_flag_choices	2019-12-02 20:53:38.864374+00
6	contenttypes	0002_remove_content_type_name	2019-12-02 20:53:38.91051+00
7	auth	0002_alter_permission_name_max_length	2019-12-02 20:53:38.935593+00
8	auth	0003_alter_user_email_max_length	2019-12-02 20:53:38.965732+00
9	auth	0004_alter_user_username_opts	2019-12-02 20:53:38.98263+00
10	auth	0005_alter_user_last_login_null	2019-12-02 20:53:39.004062+00
11	auth	0006_require_contenttypes_0002	2019-12-02 20:53:39.017791+00
12	auth	0007_alter_validators_add_error_messages	2019-12-02 20:53:39.043489+00
13	auth	0008_alter_user_username_max_length	2019-12-02 20:53:39.153542+00
14	auth	0009_alter_user_last_name_max_length	2019-12-02 20:53:39.198896+00
15	auth	0010_alter_group_name_max_length	2019-12-02 20:53:39.226522+00
16	auth	0011_update_proxy_permissions	2019-12-02 20:53:39.250758+00
17	sessions	0001_initial	2019-12-02 20:53:39.341817+00
18	knox	0001_initial	2020-04-03 12:22:38.552681+00
19	knox	0002_auto_20150916_1425	2020-04-03 12:22:39.316747+00
20	knox	0003_auto_20150916_1526	2020-04-03 12:22:39.504564+00
21	knox	0004_authtoken_expires	2020-04-03 12:22:39.531265+00
22	knox	0005_authtoken_token_key	2020-04-03 12:22:39.569092+00
23	knox	0006_auto_20160818_0932	2020-04-03 12:22:39.784065+00
24	knox	0007_auto_20190111_0542	2020-04-03 12:22:39.838801+00
25	sites	0001_initial	2020-12-13 18:38:11.711909+00
26	sites	0002_alter_domain_unique	2020-12-13 18:38:11.900316+00
27	auth	0012_alter_user_first_name_max_length	2020-12-21 17:33:35.083122+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
4oltk1ngybwsx115szottpsjwdfw9ore	NjA5ODlhYjcxMTkxOTE5YmExODYxNTVkYjRlZjA2M2JlZDc5NTk2Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmZGFiYzdhZmU0NmFlMDFmNzZjMmIzOWRlZjRiYjA4YzJkOThkNTM3In0=	2019-12-22 18:32:18.346166+00
sd7uwee6eqej7mlhrtkd3g2aagx29msk	NjA5ODlhYjcxMTkxOTE5YmExODYxNTVkYjRlZjA2M2JlZDc5NTk2Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmZGFiYzdhZmU0NmFlMDFmNzZjMmIzOWRlZjRiYjA4YzJkOThkNTM3In0=	2020-01-03 19:26:12.477173+00
aflxoep73zt5wk9u9rkfp12do8x2sc38	NTFmYjllNzRhNzY1ZDJjNThmNDNiYmQ5ZTY2MzRkZjI1N2ViYTIyOTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMjcyNTQ4YTY4ZjZlMGVhNjEyMGRlNTBmOWY0YTIzMWY2YWVjODIzIn0=	2020-04-21 19:59:05.308757+00
kk0ncw2qhilskzrvxya5n9zcg6ni5nco	NjA5ODlhYjcxMTkxOTE5YmExODYxNTVkYjRlZjA2M2JlZDc5NTk2Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmZGFiYzdhZmU0NmFlMDFmNzZjMmIzOWRlZjRiYjA4YzJkOThkNTM3In0=	2020-11-21 15:02:27.878627+00
oxoqupw4z4bisnebkqlt1n9ipejawa7s	.eJxVjMsOgjAQRf-la9PQMg_q0r3fQEpnalEDCYWV8d-VhIVu7znnvkwft7X0W9WlH8WcjTOn322I6aHTDuQep9ts0zytyzjYXbEHrfY6iz4vh_t3UGIt31qFGxHmrEIkWR12AyIAMrSBEkDnOQUFEC-E2TW5QwrqPLXgkdi8P-XuNw0:1ksthE:lrqsueTyG3_jdwkjs9bY50s8lsl_iWUo6Cm5ARWtZEE	2021-01-08 20:28:20.680136+00
g5c58nsgdmttl7v7uonl67fnn1v6wy38	NjA5ODlhYjcxMTkxOTE5YmExODYxNTVkYjRlZjA2M2JlZDc5NTk2Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmZGFiYzdhZmU0NmFlMDFmNzZjMmIzOWRlZjRiYjA4YzJkOThkNTM3In0=	2020-11-21 19:28:14.559568+00
efbn3w4v4v9ixjh8hq51ums9e6aon5ok	.eJxVjMsOgjAQRf-la9PQMg_q0r3fQEpnalEDCYWV8d-VhIVu7znnvkwft7X0W9WlH8WcjTOn322I6aHTDuQep9ts0zytyzjYXbEHrfY6iz4vh_t3UGIt31qFGxHmrEIkWR12AyIAMrSBEkDnOQUFEC-E2TW5QwrqPLXgkdi8P-XuNw0:1kxuZI:Mr_eLiYc6w0sgSj3djmYeuxSK46E_Ihc7mi68q39MHc	2021-01-22 16:24:52.696831+00
rlxph4fyy2a8ouuc4mpgsjq3j4xwo5ft	NWY5MTVkM2QzMjQ3ZTlhMTY4OTRlYzUwY2MxYjBkZTkwNjZiNjdmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYWJlZDFkOGRhZTIwZmJlMThiMDJhYjU2YzNiOTMwNWM0OGUwYmUzIn0=	2020-12-13 19:56:36.343291+00
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Data for Name: knox_authtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.knox_authtoken (digest, salt, created, user_id, expiry, token_key) FROM stdin;
53328b862df4732ee77eedc080dda1889829c892cb6aee73f538017b8ff6e36130813299387652a9bcf4129509d943a5742a6a78e203abccafe6b05db6c76f23	13cf42dc0abca46d	2020-04-08 20:09:28.456608+00	8	2020-04-09 06:09:28.455914+00	e7e427bd
8c39b83c71882130824bd8e58c2a23710145f7ce95c4f46efde7c1539b991eb5d91d1afa990ca795a48edfb0bfd54129923d2c6261f12d910b323d3940afeaa9	b17fb0ae311ee59b	2020-05-03 22:09:30.271452+00	3	\N	0f8d9d61
17567ee1787515c57e1a60df8cfeae0898e1e2a33fefd405db713f8c13d34fa2bb195c46eadfb3c3416689cbeeda015623a6d2823704d51097a777aae5a5e5b0	293ddb7951f5e015	2020-05-04 21:37:27.910266+00	3	\N	1b1fd5e8
6f2d9bfae24106ff29bcfd0be59551f2ba765998a0e5852e4e6124f81edf2602aacbc5b153c026416c35801111ac0e511bfa1748f92d5f8bf85c0c2fef4b5537	322415d6085b52a3	2020-05-04 21:43:43.618478+00	3	\N	1ea89509
da9c50801dea3d29bf78ea6e002dc812f0ab952187a0e7756040ae3623e5a856e041136b2e1d90a9f626b9ec3742a2623f418312ec727652e0403c0f55ab5662	aeeaeb23df97b6d8	2020-05-04 21:47:37.335598+00	4	\N	1e8ab17b
fb63a6ed9f6aee3c8c73496b20464ff0058806b6a73506cedc20f691b4b0548c3eb39ad031b4dc097e507b8b29ab97d4839afcf9edc4302b4e20c66675998897	875cab65f4e43c34	2020-08-21 21:46:18.615583+00	2	\N	86e6db1e
be1cfbd0a9785e6ea3dbbc385357b789de6bf07614b53c6dcd80bb3656d97eda6ceab4ab5f02aa6f3ad33b46f14cb975a5e8a99f0e8ec69b7a365b22fa23f831	60f6e3887ce51b70	2020-09-11 15:39:24.038318+00	3	\N	9fe9f33f
0f286d22551b41fcbb3d46ec7e57b2076011ffcf17b2b8484167f9e138325dfb3c1eb4f66612326287f8d41e479e2686cb56650bce2eb0f07607f851db7f9c12	689f687ec28936af	2020-04-08 20:07:07.050779+00	7	2020-04-09 06:07:07.05011+00	9e8d701d
b7eefbbb5baaa61b1a88269b7b2e5108446cc02f280d413d82d584a2d7dafb30d96210a9c0fd034f755fd25e9d9223ed6bbfa700f4bf515c15f50d337685ce59	c8160e180272cbaa	2020-04-06 20:09:30.544978+00	5	2020-04-07 06:09:30.543902+00	08918cb0
cde2e5e2601d826e02227fc4a99facf71fd4684a2d13d384bb5ae2b5d726c5db83f08a5e7f07d70941c15392627edfb99d8e0528e6e49e3032b1812e40e2f37d	7e350c7fb0cb0b2c	2020-04-06 20:26:06.450596+00	6	2020-04-07 06:26:06.450229+00	a9815395
f88e4085723e7f3fc1349fe803824f94247b21daa18a92c541a1b7a896647e4cb2d4670875be152e0a9b7760929b5f4bfbd49a2e8021fbfecfae491c5f7430c5	583b4b0c3e5bfc4b	2020-04-14 20:02:09.69469+00	3	\N	e2947b1e
5e6f73baace7171de1fb55e8dbab172d8ddb97196e9fc42d352d75847d98352000fe7a1863826c2170ff66ef5f878ae35ec98b64113f5cb7a6e90fd2972822a4	99e5efa85b66165c	2020-05-03 21:36:58.030845+00	9	\N	57fa4a4e
d9d5f60b284b12cf761429de2e077a499b806d49e4e132fafb6e240a9e1934d5dbcfef2f7ac7e865fbc67b9f31fa320f5031a0c872afcc4ae19ec59ac90e69de	185a4e15b90cc390	2020-05-03 22:17:28.745026+00	3	\N	56525261
1ccd19e1199ad04e5a6d65e50b25ffdae022505221c33f319643fef9b51a2497073d4e7ced41f9147d04ea27ed2cf03bce126d9a30d85794da96576afe1e4e65	da69393c0e302505	2020-05-04 21:46:42.994768+00	3	\N	f854f9b8
ea1fffa2c7f2e0503e00c46a265e1fc2c531a3339ce21c4e5c3a2664339bcd513822fab5322f717e31a2babf1c17350bc71ec0ce51c77cd7b554b777ccd8b7a5	6b5227300d6583bc	2020-05-04 21:50:44.886944+00	3	\N	eec375e3
19ac8685fd02941214fbc293d2d2aee4e6ae553be4f13d5f1fcafa5e9c2a262051202966d4a29df3838f4829edbf1e2a5af74e8f3221304d75dd3e50368de367	0831394da54575a4	2021-03-03 18:52:58.187469+00	1	\N	6e75bbc2
\.


--
-- Data for Name: order_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.order_items (id, order_id, product_id, amount, price, created_at, updated_at) FROM stdin;
57	9	\N	0.00	0	2020-11-12 00:05:06.860441	2021-03-03 21:12:01.124343
42	9	27	0.43	150	2020-09-13 13:51:26.148157	2021-03-03 21:12:01.099496
37	9	27	3.00	5	2020-05-22 17:56:38.839719	2021-03-03 21:12:01.191155
51	10	24	0.00	0	2020-11-11 22:19:16.122115	2021-03-03 21:12:55.41624
66	7	36	0.00	550	2021-03-13 20:58:51.299103	2021-03-13 20:58:51.299126
68	5	35	1.10	350	2021-03-16 13:30:39.743515	2021-03-21 21:13:13.665462
49	5	36	10.00	300	2020-11-10 23:26:04.934294	2021-03-21 21:18:57.490556
62	5	35	10.00	350	2021-01-08 20:09:20.679592	2021-03-21 21:18:57.532781
82	11	35	0.50	350	2021-03-22 23:44:46.781389	2021-03-22 23:44:46.781414
83	11	\N	\N	\N	2021-03-22 23:44:46.855734	2021-03-22 23:44:46.855758
84	5	37	0.45	320	2021-03-23 22:24:23.906103	2021-03-23 22:24:23.906127
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (id, customer_id, created_at, updated_at, post_cost, packet, delivery_type, address, gift) FROM stdin;
9	18	2020-05-21 20:48:00.194052	2021-03-03 21:12:01.059422	239	0	\N	jjjjjjxcbffff	
10	8	2020-05-21 19:37:47.073167	2021-03-03 21:12:55.392775	176	0	0	\N	\N
11	17	2021-03-22 23:44:46.585232	2021-03-22 23:44:46.58533	176	27	0		
7	21	2020-03-05 10:02:16.470501	2021-03-22 23:53:28.717697	\N	\N	0		
5	28	2020-02-18 12:59:32.002706	2021-03-23 22:25:28.687162	691	85	0		1931
\.


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.posts (id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (id, name, price, created_at, updated_at, weight, width, density, dollar_price, dollar_rate, width_shop, density_shop, weight_for_count, length_for_count, price_pre, image) FROM stdin;
33	Рибана с лайкрой Джинс + Сердечки	600	2021-01-08 19:31:39.405364	2021-01-08 20:31:13.144684	\N	130	240	\N	\N	\N	\N	\N	\N	\N	
34	Футер двухнитка с лайкрой Ментол	450	2021-01-08 19:33:54.390031	2021-01-08 20:31:13.170982	\N	190	240	\N	\N	\N	\N	\N	\N	\N	
37	Кулирная гладь с лайкрой Светлый оливковый	320	2021-01-08 19:37:33.718003	2021-01-08 20:31:13.271308	\N	184	170	\N	\N	\N	\N	\N	\N	\N	
27	test5	150	2020-08-22 13:54:02.865502	2021-03-03 21:12:01.164847	\N	180	170	\N	\N	\N	\N	\N	\N	\N	
24	teg24ddddd	126	2020-08-08 17:56:57.996457	2021-03-03 21:12:55.409713	\N	\N	567	\N	\N	180	190	\N	\N	\N	product/image/24/lGDb4Qwwm9g.jpg
36	Кулирная гладь с лайкрой Водный мир	550	2021-01-08 19:36:41.403481	2021-03-13 20:58:51.287226	\N	180	170	\N	\N	\N	\N	\N	\N	\N	
35	Кулирная гладь с лайкрой Лимонад	350	2021-01-08 19:36:02.603341	2021-03-26 17:25:22.384089	20.06	190	178	7.55	75.00	\N	\N	336	1.00	\N	product/image/35/WMoSptHrOhw_ztjAl4O.jpg
\.


--
-- Data for Name: schema_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.schema_migrations (version) FROM stdin;
20180122150110
20181113184241
20181104214918
20181107205124
20181105182102
20181110184058
20181104200147
20170307175831
20170204195014
20171212164638
20181105191956
20181105163237
20181106125651
20170307131224
20181111183114
20170218141850
20171213173947
20170508160343
20170506181027
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, provider, uid, encrypted_password, reset_password_token, reset_password_sent_at, remember_created_at, sign_in_count, current_sign_in_at, last_sign_in_at, current_sign_in_ip, last_sign_in_ip, confirmation_token, confirmed_at, confirmation_sent_at, unconfirmed_email, name, nickname, image, email, tokens, created_at, updated_at) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 32, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 10, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: customers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customers_id_seq', 30, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 7, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 27, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- Name: order_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_items_id_seq', 84, true);


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_seq', 11, true);


--
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.posts_id_seq', 1, false);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 37, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: ar_internal_metadata ar_internal_metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ar_internal_metadata
    ADD CONSTRAINT ar_internal_metadata_pkey PRIMARY KEY (key);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: cities cities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cities
    ADD CONSTRAINT cities_pkey PRIMARY KEY (pindex);


--
-- Name: customers customers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: knox_authtoken knox_authtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.knox_authtoken
    ADD CONSTRAINT knox_authtoken_pkey PRIMARY KEY (digest);


--
-- Name: knox_authtoken knox_authtoken_salt_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.knox_authtoken
    ADD CONSTRAINT knox_authtoken_salt_key UNIQUE (salt);


--
-- Name: order_items order_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: schema_migrations schema_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schema_migrations
    ADD CONSTRAINT schema_migrations_pkey PRIMARY KEY (version);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: index_cities_on_city; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX index_cities_on_city ON public.cities USING btree (city);


--
-- Name: index_order_items_on_order_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX index_order_items_on_order_id ON public.order_items USING btree (order_id);


--
-- Name: index_order_items_on_product_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX index_order_items_on_product_id ON public.order_items USING btree (product_id);


--
-- Name: index_orders_on_customer_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX index_orders_on_customer_id ON public.orders USING btree (customer_id);


--
-- Name: index_orders_on_delivery_type; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX index_orders_on_delivery_type ON public.orders USING btree (delivery_type);


--
-- Name: index_users_on_confirmation_token; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX index_users_on_confirmation_token ON public.users USING btree (confirmation_token);


--
-- Name: index_users_on_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX index_users_on_email ON public.users USING btree (email);


--
-- Name: index_users_on_reset_password_token; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX index_users_on_reset_password_token ON public.users USING btree (reset_password_token);


--
-- Name: index_users_on_uid_and_provider; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX index_users_on_uid_and_provider ON public.users USING btree (uid, provider);


--
-- Name: knox_authtoken_digest_188c7e77_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX knox_authtoken_digest_188c7e77_like ON public.knox_authtoken USING btree (digest varchar_pattern_ops);


--
-- Name: knox_authtoken_salt_3d9f48ac_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX knox_authtoken_salt_3d9f48ac_like ON public.knox_authtoken USING btree (salt varchar_pattern_ops);


--
-- Name: knox_authtoken_token_key_8f4f7d47; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX knox_authtoken_token_key_8f4f7d47 ON public.knox_authtoken USING btree (token_key);


--
-- Name: knox_authtoken_token_key_8f4f7d47_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX knox_authtoken_token_key_8f4f7d47_like ON public.knox_authtoken USING btree (token_key varchar_pattern_ops);


--
-- Name: knox_authtoken_user_id_e5a5d899; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX knox_authtoken_user_id_e5a5d899 ON public.knox_authtoken USING btree (user_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: knox_authtoken knox_authtoken_user_id_e5a5d899_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.knox_authtoken
    ADD CONSTRAINT knox_authtoken_user_id_e5a5d899_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

