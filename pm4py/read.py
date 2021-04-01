import warnings
from typing import Tuple

import deprecation

from pm4py.objects.bpmn.obj import BPMN
from pm4py.objects.log.obj import EventLog
from pm4py.objects.petri.obj import PetriNet, Marking
from pm4py.objects.process_tree.obj import ProcessTree

INDEX_COLUMN = "@@index"


def read_xes(file_path: str) -> EventLog:
    """
    Reads an event log in the XES standard

    Parameters
    ---------------
    file_path
        File path

    Returns
    ---------------
    log
        Event log
    """
    from pm4py.objects.log.importer.xes import importer as xes_importer
    log = xes_importer.apply(file_path)
    return log


def read_pnml(file_path: str) -> Tuple[PetriNet, Marking, Marking]:
    """
    Reads a Petri net from the .PNML format

    Parameters
    ----------------
    file_path
        File path

    Returns
    ----------------
    petri_net
        Petri net object
    initial_marking
        Initial marking
    final_marking
        Final marking
    """
    from pm4py.objects.petri.importer import importer as pnml_importer
    net, im, fm = pnml_importer.apply(file_path)
    return net, im, fm


@deprecation.deprecated(deprecated_in='2.2.2', removed_in='2.3.0',
                        details='read_petri_net is deprecated, use read_pnml instead')
def read_petri_net(file_path: str) -> Tuple[PetriNet, Marking, Marking]:
    warnings.warn('read_petri_net is deprecated, use read_pnml instead', DeprecationWarning)
    """
    Reads a Petri net from the .PNML format

    Parameters
    ----------------
    file_path
        File path

    Returns
    ----------------
    petri_net
        Petri net object
    initial_marking
        Initial marking
    final_marking
        Final marking
    """
    from pm4py.objects.petri.importer import importer as pnml_importer
    net, im, fm = pnml_importer.apply(file_path)
    return net, im, fm


def read_ptml(file_path: str) -> ProcessTree:
    """
    Reads a process tree from a .ptml file

    Parameters
    ---------------
    file_path
        File path

    Returns
    ----------------
    tree
        Process tree
    """
    from pm4py.objects.process_tree.importer import importer as tree_importer
    tree = tree_importer.apply(file_path)
    return tree


@deprecation.deprecated(deprecated_in='2.2.2', removed_in='2.3.0',
                        details='read_process_tree is deprecated, use read_ptml instead')
def read_process_tree(file_path: str) -> Tuple[PetriNet, Marking, Marking]:
    warnings.warn('read_process_tree is deprecated, use read_ptml instead', DeprecationWarning)
    """
    Reads a process tree from a .ptml file

    Parameters
    ---------------
    file_path
        File path

    Returns
    ----------------
    tree
        Process tree
    """
    from pm4py.objects.process_tree.importer import importer as tree_importer
    tree = tree_importer.apply(file_path)
    return tree


def read_dfg(file_path: str) -> Tuple[dict, dict, dict]:
    """
    Reads a DFG from a .dfg file

    Parameters
    ------------------
    file_path
        File path

    Returns
    ------------------
    dfg
        DFG
    start_activities
        Start activities
    end_activities
        End activities
    """
    from pm4py.objects.dfg.importer import importer as dfg_importer
    dfg, start_activities, end_activities = dfg_importer.apply(file_path)
    return dfg, start_activities, end_activities


def read_bpmn(file_path: str) -> BPMN:
    """
    Reads a BPMN from a .bpmn file

    Parameters
    ---------------
    file_path
        File path

    Returns
    ---------------
    bpmn_graph
        BPMN graph
    """
    from pm4py.objects.bpmn.importer import importer as bpmn_importer
    bpmn_graph = bpmn_importer.apply(file_path)
    return bpmn_graph
