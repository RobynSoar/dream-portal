const deleteBookmarkModal = new bootstrap.Modal(document.getElementById("deleteBookmarkModal"));
const deleteBookmarkButtons = document.getElementsByClassName("btn-bookmark-delete");
const deleteBookmarkConfirm = document.getElementById("deleteBookmarkConfirm");


/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteBookmarkButtons` collection:
 * - Retrieves the associated bookmark's slug upon click.
 * - Updates the `deleteBookmarkConfirm` link's href to point to the 
 *   deletion endpoint for the specific bookmark.
 * - Displays a confirmation modal (`deleteBookmarkModal`) to prompt 
 *   the user for confirmation before deletion.
 */
for (let button of deleteBookmarkButtons) {
    button.addEventListener("click", (e) => {
      let bookmarkId = e.target.getAttribute("data_id");
      deleteBookmarkConfirm.setAttribute('href', `/bookmarks/delete-bookmark/${bookmarkId}/`);
      deleteBookmarkModal.show();
    });
  }