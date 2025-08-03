package org.nonograms.pagination.model;

import org.nonograms.pagination.model.lanes.LaneGroup;

import java.util.List;

/**
 * Entire nonogram model containing a grid, row and column clues, and an identifier (for the top-left corner).
 */
public class Nonogram {

    /**
     * Top-level group of horizontal {@link org.nonograms.pagination.model.lanes.Lane lanes} (nonogram rows).
     */
    private final LaneGroup horizontalLanes;
    /**
     * Top-level group of vertical {@link org.nonograms.pagination.model.lanes.Lane lanes} (nonogram columns).
     */
    private final LaneGroup verticalLanes;

    public Nonogram() {
        this.horizontalLanes = new LaneGroup();
        this.verticalLanes = new LaneGroup();
    }

    /**
     * Populates the nonogram with the provided row and column clues.
     * @param rowClues      List of clues for the nonogram rows
     * @param columnClues   List of clues for the nonogram columns
     */
    public void populate(final List<List<Integer>> rowClues, final List<List<Integer>> columnClues) {
        horizontalLanes.populate(rowClues);
        verticalLanes.populate(columnClues);
    }

    public LaneGroup getHorizontalLanes() {
        return horizontalLanes;
    }

    public LaneGroup getVerticalLanes() {
        return verticalLanes;
    }
}
