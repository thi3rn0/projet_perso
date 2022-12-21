
-- object: public."CLASSES" | type: TABLE --
DROP TABLE IF EXISTS public."CLASSES" CASCADE;
CREATE TABLE public."CLASSES" (
	id_classe smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_classe varchar(10) NOT NULL,
	CONSTRAINT classe_pk PRIMARY KEY (id_classe)

);
-- ddl-end --
ALTER TABLE public."CLASSES" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MATIERES_CP" | type: TABLE --
DROP TABLE IF EXISTS public."MATIERES_CP" CASCADE;
CREATE TABLE public."MATIERES_CP" (
	id_matiere_cp smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_matiere_cp varchar(20) NOT NULL,
	id_classe smallint,
	CONSTRAINT "MATIERES_CP_pk" PRIMARY KEY (id_matiere_cp)

);
-- ddl-end --
ALTER TABLE public."MATIERES_CP" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_FRANCAIS_CP" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_FRANCAIS_CP" CASCADE;
CREATE TABLE public."MODULES_FRANCAIS_CP" (
	id_modules_francais_cp smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_francais_cp varchar(200) NOT NULL,
	objectif_francais_cp varchar(200) NOT NULL,
	conseil_francais_cp varchar(200),
	ressource_francais_cp varchar(200),
	id_matiere_cp smallint,
	CONSTRAINT "MODULES_FRANCAIS_CP_pk" PRIMARY KEY (id_modules_francais_cp)

);
-- ddl-end --
COMMENT ON COLUMN public."MODULES_FRANCAIS_CP".objectif_francais_cp IS E'exemple d''objectif à atteindre à la fin du module';
-- ddl-end --
ALTER TABLE public."MODULES_FRANCAIS_CP" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public.parent | type: TABLE --
DROP TABLE IF EXISTS public.parent CASCADE;
CREATE TABLE public.parent (
	id_parent smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_parent varchar(30),
	prenom_parent varchar(30),
	CONSTRAINT parent_pk PRIMARY KEY (id_parent)

);
-- ddl-end --
ALTER TABLE public.parent OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public.enfant | type: TABLE --
DROP TABLE IF EXISTS public.enfant CASCADE;
CREATE TABLE public.enfant (
	id_enfant smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	prenom_enfant varchar(30),
	id_parent smallint,
	id_classe smallint,
	CONSTRAINT enfant_pk PRIMARY KEY (id_enfant)

);
-- ddl-end --
ALTER TABLE public.enfant OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MATIERES_CE2" | type: TABLE --
DROP TABLE IF EXISTS public."MATIERES_CE2" CASCADE;
CREATE TABLE public."MATIERES_CE2" (
	id_matiere_ce2 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_matiere_ce2 varchar(20) NOT NULL,
	id_classe smallint,
	CONSTRAINT "MATIERES_CE2_pk" PRIMARY KEY (id_matiere_ce2)

);
-- ddl-end --
ALTER TABLE public."MATIERES_CE2" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_MATHS_CP" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_MATHS_CP" CASCADE;
CREATE TABLE public."MODULES_MATHS_CP" (
	id_modules_maths_cp smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_maths_cp varchar(200) NOT NULL,
	objectif_maths_cp varchar(200) NOT NULL,
	conseil_maths_cp varchar(200),
	ressource_francais_cp varchar(200),
	id_matiere_cp smallint,
	CONSTRAINT "MODULES_MATHS_CP_pk" PRIMARY KEY (id_modules_maths_cp)

);
-- ddl-end --
ALTER TABLE public."MODULES_MATHS_CP" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MATIERES_CE1" | type: TABLE --
DROP TABLE IF EXISTS public."MATIERES_CE1" CASCADE;
CREATE TABLE public."MATIERES_CE1" (
	id_matiere_ce1 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_matiere_ce1 varchar(20) NOT NULL,
	id_classe smallint,
	CONSTRAINT "MATIERES_CE1_pk" PRIMARY KEY (id_matiere_ce1)

);
-- ddl-end --
ALTER TABLE public."MATIERES_CE1" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_FRANCAIS_CE1" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_FRANCAIS_CE1" CASCADE;
CREATE TABLE public."MODULES_FRANCAIS_CE1" (
	id_module_francais_ce1 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_francais_ce1 varchar(200) NOT NULL,
	objectif_francais_ce1 varchar(200) NOT NULL,
	id_matiere_ce1 smallint,
	CONSTRAINT "MODULES_FRANCAIS_CE1_pk" PRIMARY KEY (id_module_francais_ce1)

);
-- ddl-end --
ALTER TABLE public."MODULES_FRANCAIS_CE1" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_MATHS_CE1" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_MATHS_CE1" CASCADE;
CREATE TABLE public."MODULES_MATHS_CE1" (
	id_module_maths_ce1 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_maths_ce1 varchar(200) NOT NULL,
	objectif_maths_ce1 varchar(200) NOT NULL,
	id_matiere_ce1 smallint,
	CONSTRAINT "MODULES_MATHS_CE1_pk" PRIMARY KEY (id_module_maths_ce1)

);
-- ddl-end --
ALTER TABLE public."MODULES_MATHS_CE1" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_FRANCAIS_CE2" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_FRANCAIS_CE2" CASCADE;
CREATE TABLE public."MODULES_FRANCAIS_CE2" (
	id_module_francais_ce2 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_francais_ce2 varchar(200) NOT NULL,
	objectif_francais_ce2 varchar(200) NOT NULL,
	id_matiere_ce2 smallint,
	CONSTRAINT "MODULES_FRANCAIS_CE2_pk" PRIMARY KEY (id_module_francais_ce2)

);
-- ddl-end --
ALTER TABLE public."MODULES_FRANCAIS_CE2" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_MATHS_CE2" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_MATHS_CE2" CASCADE;
CREATE TABLE public."MODULES_MATHS_CE2" (
	id_module_maths_ce2 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_maths_ce2 varchar(200) NOT NULL,
	objectif_maths_ce2 varchar(200) NOT NULL,
	id_matiere_ce2 smallint,
	CONSTRAINT "MODULES_MATHS_CE2_pk" PRIMARY KEY (id_module_maths_ce2)

);
-- ddl-end --
ALTER TABLE public."MODULES_MATHS_CE2" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MATIERES_CM1" | type: TABLE --
DROP TABLE IF EXISTS public."MATIERES_CM1" CASCADE;
CREATE TABLE public."MATIERES_CM1" (
	id_matiere_cm1 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_matiere_cm1 varchar(20) NOT NULL,
	id_classe smallint,
	CONSTRAINT "MATIERES_CM1_pk" PRIMARY KEY (id_matiere_cm1)

);
-- ddl-end --
ALTER TABLE public."MATIERES_CM1" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_FRANCAIS_CM1" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_FRANCAIS_CM1" CASCADE;
CREATE TABLE public."MODULES_FRANCAIS_CM1" (
	id_module_francais_cm1 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_francais_cm1 varchar(200) NOT NULL,
	objectif_francais_cm1 varchar(200) NOT NULL,
	id_matiere_cm1 smallint,
	CONSTRAINT "MODULES_FRANCAIS_CM1_pk" PRIMARY KEY (id_module_francais_cm1)

);
-- ddl-end --
ALTER TABLE public."MODULES_FRANCAIS_CM1" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_MATHS_CM1" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_MATHS_CM1" CASCADE;
CREATE TABLE public."MODULES_MATHS_CM1" (
	id_module_maths_cm1 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_maths_cm1 varchar(200) NOT NULL,
	objectif_maths_cm1 varchar(200) NOT NULL,
	id_matiere_cm1 smallint,
	CONSTRAINT "MODULES_MATHS_CM1_pk" PRIMARY KEY (id_module_maths_cm1)

);
-- ddl-end --
ALTER TABLE public."MODULES_MATHS_CM1" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MATIERES_CM2" | type: TABLE --
DROP TABLE IF EXISTS public."MATIERES_CM2" CASCADE;
CREATE TABLE public."MATIERES_CM2" (
	id_matiere_cm2 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_matiere_cm2 varchar(20) NOT NULL,
	id_classe smallint,
	CONSTRAINT "MATIERES_CM2_pk" PRIMARY KEY (id_matiere_cm2)

);
-- ddl-end --
ALTER TABLE public."MATIERES_CM2" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_FRANCAIS_CM2" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_FRANCAIS_CM2" CASCADE;
CREATE TABLE public."MODULES_FRANCAIS_CM2" (
	id_module_francais_cm2 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_francais_cm2 varchar(200) NOT NULL,
	objectif_francais_cm2 varchar(200) NOT NULL,
	id_matiere_cm2 smallint,
	CONSTRAINT "MODULES_FRANCAIS_CM2_pk" PRIMARY KEY (id_module_francais_cm2)

);
-- ddl-end --
ALTER TABLE public."MODULES_FRANCAIS_CM2" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: public."MODULES_MATHS_CM2" | type: TABLE --
DROP TABLE IF EXISTS public."MODULES_MATHS_CM2" CASCADE;
CREATE TABLE public."MODULES_MATHS_CM2" (
	id_module_maths_cm2 smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom_module_maths_cm2 varchar(200) NOT NULL,
	objectif_maths_cm2 varchar(200) NOT NULL,
	id_matiere_cm2 smallint,
	CONSTRAINT "MODULES_MATHS_CM2_pk" PRIMARY KEY (id_module_maths_cm2)

);
-- ddl-end --
ALTER TABLE public."MODULES_MATHS_CM2" OWNER TO dev_apprentissage;
-- ddl-end --

-- object: "CLASSES_fk" | type: CONSTRAINT --
ALTER TABLE public."MATIERES_CP" DROP CONSTRAINT IF EXISTS "CLASSES_fk" CASCADE;
ALTER TABLE public."MATIERES_CP" ADD CONSTRAINT "CLASSES_fk" FOREIGN KEY (id_classe)
REFERENCES public."CLASSES" (id_classe) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "CLASSES_fk" | type: CONSTRAINT --
ALTER TABLE public."MATIERES_CE1" DROP CONSTRAINT IF EXISTS "CLASSES_fk" CASCADE;
ALTER TABLE public."MATIERES_CE1" ADD CONSTRAINT "CLASSES_fk" FOREIGN KEY (id_classe)
REFERENCES public."CLASSES" (id_classe) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "CLASSES_fk" | type: CONSTRAINT --
ALTER TABLE public."MATIERES_CM2" DROP CONSTRAINT IF EXISTS "CLASSES_fk" CASCADE;
ALTER TABLE public."MATIERES_CM2" ADD CONSTRAINT "CLASSES_fk" FOREIGN KEY (id_classe)
REFERENCES public."CLASSES" (id_classe) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "CLASSES_fk" | type: CONSTRAINT --
ALTER TABLE public."MATIERES_CM1" DROP CONSTRAINT IF EXISTS "CLASSES_fk" CASCADE;
ALTER TABLE public."MATIERES_CM1" ADD CONSTRAINT "CLASSES_fk" FOREIGN KEY (id_classe)
REFERENCES public."CLASSES" (id_classe) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "CLASSES_fk" | type: CONSTRAINT --
ALTER TABLE public."MATIERES_CE2" DROP CONSTRAINT IF EXISTS "CLASSES_fk" CASCADE;
ALTER TABLE public."MATIERES_CE2" ADD CONSTRAINT "CLASSES_fk" FOREIGN KEY (id_classe)
REFERENCES public."CLASSES" (id_classe) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: parent_fk | type: CONSTRAINT --
ALTER TABLE public.enfant DROP CONSTRAINT IF EXISTS parent_fk CASCADE;
ALTER TABLE public.enfant ADD CONSTRAINT parent_fk FOREIGN KEY (id_parent)
REFERENCES public.parent (id_parent) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "CLASSES_fk" | type: CONSTRAINT --
ALTER TABLE public.enfant DROP CONSTRAINT IF EXISTS "CLASSES_fk" CASCADE;
ALTER TABLE public.enfant ADD CONSTRAINT "CLASSES_fk" FOREIGN KEY (id_classe)
REFERENCES public."CLASSES" (id_classe) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: enfant_uq | type: CONSTRAINT --
ALTER TABLE public.enfant DROP CONSTRAINT IF EXISTS enfant_uq CASCADE;
ALTER TABLE public.enfant ADD CONSTRAINT enfant_uq UNIQUE (id_classe);
-- ddl-end --

-- object: "MATIERES_CP_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_FRANCAIS_CP" DROP CONSTRAINT IF EXISTS "MATIERES_CP_fk" CASCADE;
ALTER TABLE public."MODULES_FRANCAIS_CP" ADD CONSTRAINT "MATIERES_CP_fk" FOREIGN KEY (id_matiere_cp)
REFERENCES public."MATIERES_CP" (id_matiere_cp) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "MATIERES_CP_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_MATHS_CP" DROP CONSTRAINT IF EXISTS "MATIERES_CP_fk" CASCADE;
ALTER TABLE public."MODULES_MATHS_CP" ADD CONSTRAINT "MATIERES_CP_fk" FOREIGN KEY (id_matiere_cp)
REFERENCES public."MATIERES_CP" (id_matiere_cp) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "MATIERES_CE1_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_FRANCAIS_CE1" DROP CONSTRAINT IF EXISTS "MATIERES_CE1_fk" CASCADE;
ALTER TABLE public."MODULES_FRANCAIS_CE1" ADD CONSTRAINT "MATIERES_CE1_fk" FOREIGN KEY (id_matiere_ce1)
REFERENCES public."MATIERES_CE1" (id_matiere_ce1) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "MATIERES_CE1_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_MATHS_CE1" DROP CONSTRAINT IF EXISTS "MATIERES_CE1_fk" CASCADE;
ALTER TABLE public."MODULES_MATHS_CE1" ADD CONSTRAINT "MATIERES_CE1_fk" FOREIGN KEY (id_matiere_ce1)
REFERENCES public."MATIERES_CE1" (id_matiere_ce1) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "MATIERES_CM1_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_FRANCAIS_CM1" DROP CONSTRAINT IF EXISTS "MATIERES_CM1_fk" CASCADE;
ALTER TABLE public."MODULES_FRANCAIS_CM1" ADD CONSTRAINT "MATIERES_CM1_fk" FOREIGN KEY (id_matiere_cm1)
REFERENCES public."MATIERES_CM1" (id_matiere_cm1) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "MATIERES_CM1_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_MATHS_CM1" DROP CONSTRAINT IF EXISTS "MATIERES_CM1_fk" CASCADE;
ALTER TABLE public."MODULES_MATHS_CM1" ADD CONSTRAINT "MATIERES_CM1_fk" FOREIGN KEY (id_matiere_cm1)
REFERENCES public."MATIERES_CM1" (id_matiere_cm1) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "MATIERES_CE2_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_FRANCAIS_CE2" DROP CONSTRAINT IF EXISTS "MATIERES_CE2_fk" CASCADE;
ALTER TABLE public."MODULES_FRANCAIS_CE2" ADD CONSTRAINT "MATIERES_CE2_fk" FOREIGN KEY (id_matiere_ce2)
REFERENCES public."MATIERES_CE2" (id_matiere_ce2) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "MATIERES_CE2_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_MATHS_CE2" DROP CONSTRAINT IF EXISTS "MATIERES_CE2_fk" CASCADE;
ALTER TABLE public."MODULES_MATHS_CE2" ADD CONSTRAINT "MATIERES_CE2_fk" FOREIGN KEY (id_matiere_ce2)
REFERENCES public."MATIERES_CE2" (id_matiere_ce2) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "MATIERES_CM2_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_FRANCAIS_CM2" DROP CONSTRAINT IF EXISTS "MATIERES_CM2_fk" CASCADE;
ALTER TABLE public."MODULES_FRANCAIS_CM2" ADD CONSTRAINT "MATIERES_CM2_fk" FOREIGN KEY (id_matiere_cm2)
REFERENCES public."MATIERES_CM2" (id_matiere_cm2) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "MATIERES_CM2_fk" | type: CONSTRAINT --
ALTER TABLE public."MODULES_MATHS_CM2" DROP CONSTRAINT IF EXISTS "MATIERES_CM2_fk" CASCADE;
ALTER TABLE public."MODULES_MATHS_CM2" ADD CONSTRAINT "MATIERES_CM2_fk" FOREIGN KEY (id_matiere_cm2)
REFERENCES public."MATIERES_CM2" (id_matiere_cm2) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --


