package org.nonograms.pagination.model.lanes;

import org.nonograms.pagination.model.lanes.laneparts.CluesLanePart;
import org.nonograms.pagination.model.lanes.laneparts.GridLanePart;

import java.util.List;

/**
 * An individual lane object. "Lanes" is a collective term for "rows" and "columns".
 * Contains a clues part and a grid part (which essentially just consists of cells).
 */
public final class Lane extends LaneNode {
    private final CluesLanePart cluesLanePart;
    private final GridLanePart gridLanePart;

    public Lane(final List<Integer> clueValues) {
        this.cluesLanePart = new CluesLanePart(clueValues);
        this.gridLanePart = new GridLanePart();
    }

    public CluesLanePart getCluesLanePart() {
        return cluesLanePart;
    }

    public GridLanePart getGridLanePart() {
        return gridLanePart;
    }
}
