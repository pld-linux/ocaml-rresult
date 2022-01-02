#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Result value combinators for OCaml
Summary(pl.UTF-8):	Kombinatory wartości wyników dla OCamla
Name:		ocaml-rresult
Version:	0.7.0
Release:	1
License:	ISC
Group:		Libraries
Source0:	https://erratique.ch/software/rresult/releases/rresult-%{version}.tbz
# Source0-md5:	7f6139c00926e09f6d1aa7efdcf2e703
URL:		https://erratique.ch/software/rresult
BuildRequires:	ocaml >= 1:4.08.0
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ocamlbuild
BuildRequires:	ocaml-topkg >= 1.0.3
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Rresult is an OCaml module for handling computation results and errors
in an explicit and declarative manner, without resorting to
exceptions. It defines combinators to operate on the "result" type
available from OCaml 4.03 in the standard library.

OCaml 4.08 provides the Stdlib.Result module which you should prefer
to Rresult.

This package contains files needed to run bytecode executables using
rresult library.

%description -l pl.UTF-8
Rresult to moduł OCamla do obsługi wyników obliczeń i błędów w sposób
jawny i deklaratywny, bez uciekania się do wyjątków. Definiuje
kombinatory operujące na typie "result" dostępnym w bibliotece
standardowej OCamla od wersji 4.03.

OCaml 4.08 udostępnia moduł Stdlib.Result, który powinien być
preferowany względem Rresult.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki rresult.

%package devel
Summary:	Result value combinators for OCaml - development part
Summary(pl.UTF-8):	Kombinatory wartości wyników dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
rresult library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki rresult.

%prep
%setup -q -n rresult-%{version}

%build
ocaml pkg/pkg.ml build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/rresult

cp -p _build/pkg/META _build/opam $RPM_BUILD_ROOT%{_libdir}/ocaml/rresult
cp -p _build/src/*.{cma,cmi,cmt,cmti,mli} $RPM_BUILD_ROOT%{_libdir}/ocaml/rresult
%if %{with ocaml_opt}
cp -p _build/src/*.{a,cmxs,cmx,cmxa} $RPM_BUILD_ROOT%{_libdir}/ocaml/rresult
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/rresult
%{_libdir}/ocaml/rresult/META
%{_libdir}/ocaml/rresult/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/rresult/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/rresult/*.cmi
%{_libdir}/ocaml/rresult/*.cmt
%{_libdir}/ocaml/rresult/*.cmti
%{_libdir}/ocaml/rresult/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/rresult/rresult.a
%{_libdir}/ocaml/rresult/rresult_top.a
%{_libdir}/ocaml/rresult/*.cmx
%{_libdir}/ocaml/rresult/*.cmxa
%endif
%{_libdir}/ocaml/rresult/opam
