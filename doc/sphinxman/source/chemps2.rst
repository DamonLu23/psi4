.. #
.. # @BEGIN LICENSE
.. #
.. # Psi4: an open-source quantum chemistry software package
.. #
.. # Copyright (c) 2007-2016 The Psi4 Developers.
.. #
.. # The copyrights for code used from other parties are included in
.. # the corresponding files.
.. #
.. # This program is free software; you can redistribute it and/or modify
.. # it under the terms of the GNU General Public License as published by
.. # the Free Software Foundation; either version 2 of the License, or
.. # (at your option) any later version.
.. #
.. # This program is distributed in the hope that it will be useful,
.. # but WITHOUT ANY WARRANTY; without even the implied warranty of
.. # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
.. # GNU General Public License for more details.
.. #
.. # You should have received a copy of the GNU General Public License along
.. # with this program; if not, write to the Free Software Foundation, Inc.,
.. # 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
.. #
.. # @END LICENSE
.. #

.. include:: autodoc_abbr_options_c.rst

.. index:: CheMPS2
.. _`sec:chemps2`:

Interface to CheMPS2 by S. Wouters
==================================

.. codeauthor:: Sebastian Wouters
.. sectionauthor:: Lori A. Burns

*Module:* :ref:`Keywords <apdx:dmrg>`, :ref:`PSI Variables <apdx:dmrg_psivar>`, :ref:`Samples <apdx:testSuitedmrg>`

.. comment|PSIfour| contains code to interface to the CheMPS2
.. library of S. Wouters, which is based at `GitHub
.. <https://github.com/SebWouters/CheMPS2>`_. Consult the excellent
.. `documentation <http://sebwouters.github.io/CheMPS2/>`_ for using and
.. `citing <http://sebwouters.github.io/CheMPS2/publications.html>`_ the library.

.. image:: https://img.shields.io/badge/home-CheMPS2-5077AB.svg
   :target: https://github.com/SebWouters/CheMPS2

.. raw:: html

   <br>

.. image:: https://img.shields.io/badge/docs-latest-5077AB.svg
   :target: http://sebwouters.github.io/CheMPS2/index.html

.. note:: As of late June 2016, DMRG keywords in |PSIfour| have been
   realigned with those of the chemps2 executable, plus a
   "dmrg\_" prefix. The only exceptions are the orbital space
   |PSIfour| keywords |globals__restricted_docc| (formerly
   CheMPS2 used |globals__frozen_docc|, contrary to its
   definition) and |globals__active| which are passed along to
   CheMPS2 keywords ``NOCC`` and ``NACT``. A `translation table
   <https://github.com/psi4/psi4/issues/150#issuecomment-228951911>`_
   is available.

Installation
~~~~~~~~~~~~

**Binary**

* .. image:: https://img.shields.io/badge/Anaconda%20Cloud-1.7.1-5077AB.svg
     :target: https://anaconda.org/psi4/chemps2

* CheMPS2 is available as a conda package for Linux and macOS.

* If using the |PSIfour| binary, CheMPS2 has already been installed alongside.

* If using |PSIfour| built from source, and anaconda or miniconda has
  already been installed (instructions at :ref:`sec:quickconda`),
  CheMPS2 can be obtained through ``conda install chemps2``.
  Then enable it as a feature with :makevar:`ENABLE_CheMPS2`,
  hint its location with :makevar:`CMAKE_PREFIX_PATH`,
  and rebuild |PSIfour| to detect CheMPS2 and activate dependent code.

* To remove a conda installation, ``conda remove chemps2``.

**Source**

* .. image:: https://img.shields.io/github/tag/SebWouters/chemps2.svg?maxAge=2592000
     :target: https://github.com/SebWouters/chemps2

* If using |PSIfour| built from source and you want CheMPS2 built from
  from source also,
  enable it as a feature with :makevar:`ENABLE_CheMPS2`,
  and let the build system fetch and build it and activate dependent code.

Methods
~~~~~~~

.. _`table:chemps2_calls`:

.. table:: Density matrix renormalization group capabilities of |PSIfour| through CheMPS2

    +-------------------------+--------------------------------------------------------------+----------------------+----------------------+
    | name                    | calls method                                                 |  Energy              | Gradient             |
    +=========================+==============================================================+======================+======================+
    | dmrg-ci                 | DMRG configuration interaction (CI)                          | RHF/ROHF             | ---                  |
    +-------------------------+--------------------------------------------------------------+----------------------+----------------------+
    | dmrg-scf                | DMRG complete active space SCF (CASSCF)                      | RHF/ROHF             | ---                  |
    +-------------------------+--------------------------------------------------------------+----------------------+----------------------+
    | dmrg-caspt2             | DMRG CAS with 2nd-order perturbation theory (CASPT2)         | RHF/ROHF             | ---                  |
    +-------------------------+--------------------------------------------------------------+----------------------+----------------------+

DMRG Keywords
~~~~~~~~~~~~~

.. include:: /autodir_options_c/dmrg__dmrg_caspt2_calc.rst
.. include:: /autodir_options_c/dmrg__dmrg_caspt2_imag.rst
.. include:: /autodir_options_c/dmrg__dmrg_caspt2_ipea.rst
.. include:: /autodir_options_c/dmrg__dmrg_caspt2_orbs.rst
.. include:: /autodir_options_c/dmrg__dmrg_diis.rst
.. include:: /autodir_options_c/dmrg__dmrg_diis_write.rst
.. include:: /autodir_options_c/dmrg__dmrg_excitation.rst
.. include:: /autodir_options_c/dmrg__dmrg_irrep.rst
.. include:: /autodir_options_c/dmrg__dmrg_local_init.rst
.. include:: /autodir_options_c/dmrg__dmrg_molden_write.rst
.. include:: /autodir_options_c/dmrg__dmrg_mps_write.rst
.. include:: /autodir_options_c/dmrg__dmrg_multiplicity.rst
.. include:: /autodir_options_c/dmrg__dmrg_opdm_ao_print.rst
.. include:: /autodir_options_c/dmrg__dmrg_print_corr.rst
.. include:: /autodir_options_c/dmrg__dmrg_scf_active_space.rst
.. include:: /autodir_options_c/dmrg__dmrg_scf_diis_thr.rst
.. include:: /autodir_options_c/dmrg__dmrg_scf_grad_thr.rst
.. include:: /autodir_options_c/dmrg__dmrg_scf_max_iter.rst
.. include:: /autodir_options_c/dmrg__dmrg_scf_state_avg.rst
.. include:: /autodir_options_c/dmrg__dmrg_sweep_dvdson_rtol.rst
.. include:: /autodir_options_c/dmrg__dmrg_sweep_energy_conv.rst
.. include:: /autodir_options_c/dmrg__dmrg_sweep_max_sweeps.rst
.. include:: /autodir_options_c/dmrg__dmrg_sweep_noise_prefac.rst
.. include:: /autodir_options_c/dmrg__dmrg_sweep_states.rst
.. include:: /autodir_options_c/dmrg__dmrg_unitary_write.rst
